from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.admin import admin

from app.extensions import db
from app.models import User, Loan, Announcement


@admin.before_request
def restrict_admin():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    if current_user.role != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('member.dashboard'))

@admin.route('/dashboard')
@login_required
def dashboard():

    members = User.query.filter_by(role='member').all()

    pending_members = User.query.filter_by(
        approved=False,
        role='member'
    ).all()

    loans = Loan.query.order_by(Loan.created_at.desc()).all()

    announcements = Announcement.query.all()

    return render_template(
        'admin/dashboard.html',
        members=members,
        pending_members=pending_members,
        loans=loans,
        announcements=announcements
    )

@admin.route('/approve-member/<int:id>')
@login_required
def approve_member(id):

    user = User.query.get_or_404(id)

    user.approved = True

    db.session.commit()

    flash('Member approved successfully', 'success')

    return redirect(url_for('admin.dashboard'))

@admin.route('/approve-loan/<int:id>')
@login_required
def approve_loan(id):

    loan = Loan.query.get_or_404(id)

    loan.status = 'Approved'

    db.session.commit()

    flash('Loan approved successfully', 'success')

    return redirect(url_for('admin.dashboard'))

@admin.route('/reject-loan/<int:id>')
@login_required
def reject_loan(id):

    loan = Loan.query.get_or_404(id)

    loan.status = 'Rejected'

    db.session.commit()

    flash('Loan rejected', 'error')

    return redirect(url_for('admin.dashboard'))

@admin.route('/announcement', methods=['POST'])
@login_required
def add_announcement():

    title = request.form.get('title')
    message = request.form.get('message')

    announcement = Announcement(
        title=title,
        message=message
    )

    db.session.add(announcement)
    db.session.commit()

    flash('Announcement added', 'success')

    return redirect(url_for('admin.dashboard'))
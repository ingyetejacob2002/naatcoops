from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.extensions import db
from app.models import Savings, Loan, Announcement
from app.member.forms import SavingsForm, LoanForm

from app.member import member

@member.route('/dashboard')
@login_required
def dashboard():

    savings = Savings.query.filter_by(user_id=current_user.id).all()

    loans = Loan.query.filter_by(user_id=current_user.id).all()

    announcements = Announcement.query.order_by(
        Announcement.created_at.desc()
    ).all()

    total_savings = sum(item.amount for item in savings)
    return render_template(
        'member/dashboard.html',
        savings=savings,
        loans=loans,
        announcements=announcements,
        total_savings=total_savings
    )
@member.route('/savings', methods=['GET', 'POST'])
@login_required
def savings():
    form = SavingsForm()

    if form.validate_on_submit():

        new_saving = Savings(
            amount=form.amount.data,
            user_id=current_user.id
        )

        db.session.add(new_saving)
        db.session.commit()

        flash('Savings added successfully', 'success')

        return redirect(url_for('member.dashboard'))

    return render_template('member/savings.html', form=form)

@member.route('/apply-loan', methods=['GET', 'POST'])
@login_required
def apply_loan():
    form = LoanForm()

    if form.validate_on_submit():

        loan = Loan(
            amount=form.amount.data,
            duration=form.duration.data,
            reason=form.reason.data,
            user_id=current_user.id
        )

        db.session.add(loan)
        db.session.commit()

        flash('Loan application submitted', 'success')

        return redirect(url_for('member.dashboard'))

    return render_template('member/apply_loan.html', form=form)
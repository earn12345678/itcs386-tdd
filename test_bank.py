import pytest

from bank import BankAccount, InsufficientFunds


@pytest.fixture
def account():
    return BankAccount("customer", 100)


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_overdraft(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(101)
    assert account.balance == 100


def test_starting_balance_is_fresh(account):
    assert account.balance == 100


def test_deposit_zero(account):
    with pytest.raises(ValueError, match="positive"):
        account.deposit(0)
    assert account.balance == 100


def test_empty_account_by_withdrawing_all(account):
    account.withdraw(account.balance)
    assert account.balance == 0


def test_withdraw_twice(account):
    account.withdraw(35)
    assert account.balance == 65
    account.withdraw(15)
    assert account.balance == 50


def test_ten_percent_interest(account):
    account.add_interest(0.1)
    assert account.balance == pytest.approx(110)

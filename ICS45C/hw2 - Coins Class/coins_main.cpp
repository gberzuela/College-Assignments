// coins_main.cpp
#include "Coins.h"

const int CENTS_FOR_CHIPS = 68, DEPOSIT = 205;

// Buying a bag of chips
void payChips(Coins & pocket, Coins & piggyBank)
{
    Coins payForChips =
	pocket.extract_exact_change(coins_required_for_cents(CENTS_FOR_CHIPS));
    cout << "I bought a bag of chips for " << CENTS_FOR_CHIPS << " cents using " <<
	payForChips << ".\nI have " << pocket << " left in my pocket." << endl;
}

// Depositting @2.05 from piggyBank to pocket
void deposit(Coins & pocket, Coins & piggyBank)
{
    Coins deposit =
	piggyBank.extract_exact_change(coins_required_for_cents(DEPOSIT));
    pocket.deposit_coins(deposit);
    cout << "I transferred @2.05 from my piggyBank to my pocket.\nI have " <<
	pocket << " in my pocket " << piggyBank << " in my piggyBank." << endl;
}

// You find loose change in your sofa (Coins(10,10,10,10)) and put it in the piggyBank
void sofaChange(Coins & pocket, Coins & piggyBank)
{
    Coins change(10,10,10,10);
    piggyBank.deposit_coins(change);
    float total = 
	(float)piggyBank.total_value_in_cents() / 100;
    cout << "While vacuuming, I find 10q, 10d, 10n, and 10p and deposit it them in my piggyBank.\n" <<
	"I have " << "$" << total << " in my piggyBank." << endl;
}

int main()
{
    // Creating two Coins objects
    Coins pocket(5, 3, 6, 8);
    Coins piggyBank(50, 50, 50, 50);
    cout << "Starting pocket is " << pocket << ".\nStarting piggyBank is " << piggyBank << "." << endl;
    
    // Order of events: Buy bag of chips -> Deposit $2.05 -> Find loose change
    payChips(pocket, piggyBank);
    deposit(pocket, piggyBank);
    sofaChange(pocket, piggyBank);
    return 0;
}

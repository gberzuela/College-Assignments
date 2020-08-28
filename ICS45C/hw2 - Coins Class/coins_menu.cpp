#include "Coins.h"

void presentMenu()
{
  cout << "   * * * * * * * * * * * * * * * * * * * * * * * *\n"
       << "   *   		myCoins MENU			 *\n"
       << "   *					  	 *\n"
       << "   *   OPTION				ENTER	 *\n"
       << "   *						 *\n"
       << "   *   Deposit Coins  			D or d	 *\n"
       << "   *   Extract	Coins			E or e	 *\n"
       << "   *   Print Total Coins and Value	P or p	 *\n"
       << "   *						 *\n"
       << "   *   Quit				Q or q	 *\n"
       << "   *				             	 *\n"
       << "   * * * * * * * * * * * * * * * * * * * * * * * *\n";
}

char getUser(const char * prompt)
{
    char user;
    cout << prompt;
    cin >> user;
    return user;
}

bool evaluateCommand(Coins & myCoins, char user)
{
    switch(user)
    {
	case 'D': case 'd':
	{
	    cout << "You have chosen to deposit. Please enter how many cents you would like to deposit." << endl;
	    int cent;
	    cin >> cent;
	    Coins cents = coins_required_for_cents(cent);
	    myCoins.deposit_coins(cents);
	    cout << "You have depositted " << cent << " cents." << endl;
	    return true;
	}
	case 'E': case 'e':
	{
	    cout << "You have chose to extract. Please enter how many cents you would like to extract." << endl;
	    int extract;
	    cin >> extract;
	    if (extract > myCoins.total_value_in_cents())
	    {
		cout << "You cannot extract more than you own." << endl;
		break;
	    }
	    else
	    {
		Coins extracts = coins_required_for_cents(extract);
		myCoins.extract_exact_change(extracts);
		cout << "You have successfully extracted " << extract << " cents." << endl;
		break;
	    }
	    return true;
	}
	case 'P': case 'p':
	{
	    float total = (float) myCoins.total_value_in_cents() / 100;
	    cout << "You have chosen to print. You have " << myCoins << ". Total: $" << total << endl;
	    return true;
	}
	case 'Q': case 'q':
	{
	    cout << "You have chosen to quite. Program will end now. Goodbye!" << endl;
	    return false;
	}
	default:
	{
	    cout << "Invalid input." << endl;
	    return true;
	}
    }
}

int main()
{
    Coins myCoins = Coins(0,0,0,0);
    cout << "Welcome to the interactive coin handling program!" << endl;
    bool repeat = true;
    while (repeat)
    {
	presentMenu();
	char user = getUser("Please enter a command: ");
	repeat = evaluateCommand(myCoins, user);
    }
    return 0;
}

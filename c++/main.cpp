#include<iostream>
#include "Thruster.h"

using namespace std;

int main() {
    Thruster TH;
    cout<< "Initial Status: "<<TH.getStatus()<<endl;

    TH.setSpeed(50);
    cout<<"Speed without Power: "<<TH.getSpeed()<<" "<<TH.getStatus()<<endl;

    TH.setPower(true);
    TH.setSpeed(75);
    cout<<"Powered up and running: "<<TH.getStatus()<<endl;

    TH.setSpeed(150);
    cout<< "Overlimit: "<<TH.getStatus()<<endl;

    return 0;
}
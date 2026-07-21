//
// Created by ziad on 20‏/7‏/2026.
//

#ifndef C_THRUSTER_H
#define C_THRUSTER_H

#include <string>
using namespace std;
class Thruster {
private:
    int speed;
    bool isPowered;
    string Status;
    void updateStatus();
public:
    Thruster();
    void setPower(bool power);
    void setSpeed(int newSpeed);
    int getSpeed() const;
    string getStatus() const;
};


#endif //C_THRUSTER_H

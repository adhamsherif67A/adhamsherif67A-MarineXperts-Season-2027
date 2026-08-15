#ifndef THRUSTER_HPP
#define THRUSTER_HPP

class Thruster
{
private:
    int speed;

public:
    Thruster();

    void setSpeed(int new_speed);
    int getSpeed() const;
    void getStatus() const;
};

#endif
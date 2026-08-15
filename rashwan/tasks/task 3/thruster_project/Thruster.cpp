#include "Thruster.hpp"
#include <iostream>

Thruster::Thruster()
{
    speed = 0;
}

void Thruster::setSpeed(int new_speed)
{
    speed = new_speed;
}

int Thruster::getSpeed() const
{
    return speed;
}

void Thruster::getStatus() const
{
    if (speed > 0)
    {
        std::cout << "Forward" << std::endl;
    }
    else if (speed < 0)
    {
        std::cout << "Reverse" << std::endl;
    }
    else
    {
        std::cout << "Stopped" << std::endl;
    }
}
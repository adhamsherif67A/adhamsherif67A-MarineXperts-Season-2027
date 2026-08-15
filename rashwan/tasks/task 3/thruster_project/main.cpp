#include <iostream>
#include "Thruster.hpp"

int main()
{
    Thruster thruster;

    std::cout << "Initial speed: "
              << thruster.getSpeed()
              << std::endl;

    thruster.getStatus();

    thruster.setSpeed(500);

    std::cout << "Current speed: "
              << thruster.getSpeed()
              << std::endl;

    thruster.getStatus();

    thruster.setSpeed(-300);

    std::cout << "Current speed: "
              << thruster.getSpeed()
              << std::endl;

    thruster.getStatus();

    return 0;
}
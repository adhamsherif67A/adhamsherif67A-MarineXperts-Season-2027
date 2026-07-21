//
// Created by ziad on 20‏/7‏/2026.
//

#include "Thruster.h"

Thruster::Thruster() {
    speed = 0;
    isPowered = false;
    Status = "OFF";
}

#include <filesystem>

void  Thruster::setPower(bool power) {
    isPowered = power;
    if (!isPowered) {
        speed = 0;
    }
    updateStatus();
}
void Thruster::setSpeed(int newSpeed) {
    if (isPowered) {
        if (newSpeed > 100) {
            speed = 100;
        }
        else if (newSpeed < 0) {
            speed = 0;
        }
        else {
            speed = newSpeed;
        }
    }
    updateStatus();
}
int Thruster::getSpeed() const {
    return speed;
}
string Thruster::getStatus() const {
    return Status;
}
void Thruster::updateStatus() {
    if (!isPowered) {
        Status = "OFF";
    }
    else {
        Status = "ON - Speed: " + to_string(speed) + "%";
    }
}

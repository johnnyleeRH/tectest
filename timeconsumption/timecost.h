#pragma once

#include <iostream>
#include <iomanip>
#include <vector>
#include <numeric>
#include <chrono>
#include <string>


class TimeCost
{
public:
    TimeCost()
    {
        beg_ = std::chrono::system_clock::now();
    }
    TimeCost(const std::string &flag) : str_(flag)
    {
        beg_ = std::chrono::system_clock::now();
    }
    void SetEndTime()
    {
        endset = true;
        end_ = std::chrono::system_clock::now();
    }
    ~TimeCost()
    {
        if (!endset)
            end_ = std::chrono::system_clock::now();
        std::chrono::duration<double> diff = end_ - beg_;
        std::cout << str_ << " timecost " << diff.count() * 1000 << " msec" << std::endl;
    }

private:
    std::chrono::time_point<std::chrono::system_clock> beg_;
    std::chrono::time_point<std::chrono::system_clock> end_;
    bool endset = false;
    std::string str_;
};
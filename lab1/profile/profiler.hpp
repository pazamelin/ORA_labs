#pragma once

#include "../tests/debug.hpp"

#include <chrono>
#include <iostream>
#include <optional>
#include <string>
#include <sstream>
#include <random>
#include <limits>


namespace profiler
{
    class AccumulateDuration
    {
    public:
        explicit AccumulateDuration(double& accumulator)
        : accumulator{accumulator}, start{std::chrono::steady_clock::now()}
        { }

        ~AccumulateDuration()
        {
            auto finish = std::chrono::steady_clock::now();
            std::chrono::duration<double> duration = finish - start;
            accumulator += duration.count();
            int x = 1;
        }

    private:
        std::chrono::steady_clock::time_point start;
        double& accumulator;
    };

} // namespace profiler

#ifndef UNIQ_ID
#define UNIQ_ID_IMPL(lineno) _a_local_var_##lineno
#define UNIQ_ID(lineno) UNIQ_ID_IMPL(lineno)
#endif

#define ACCUMULATE_DURATION(accumulator) \
profiler::AccumulateDuration UNIQ_ID(__LINE__){accumulator};

namespace profiler
{
    struct profile_statistic
    {
        std::size_t text_size;
        std::vector<std::size_t> pattern_sizes;       
        std::vector<double> time_for_pattern_size;
        std::int operations = 0;
    };

    template <typename Algorithm>
    std::vector<profile_statistic> profile(Algorithm algorithm,
     std::size_t text_size_min,
     std::size_t text_size_max,
     std::size_t text_size_step,
     std::size_t pattern_size_min,
     std::size_t pattern_size_max,
     std::size_t pattern_size_step,
     std::size_t iterations_per_size_pair                                  
     )
    {
        std::vector<profile_statistic> result;

        const std::string symbols("abcdefghijklmnopqrstuvwxyz");

        std::mt19937 gen(get_seed());
        std::uniform_int_distribution<> symbols_dist(0, static_cast<int>(symbols.size()) - 1);
        std::uniform_int_distribution<> pattern_occurrence_dist(0, 1);

        auto get_random_string = [&](std::size_t size)
        {
            std::string result;
            result.reserve(size);
            for (std::size_t i = 0; i < size; i++)
            {
                result.push_back(symbols[symbols_dist(gen)]);
            }

            return result;
        };

        auto insert_pattern = [&](std::string& str, const std::string& pattern, std::size_t pos)
        {
            for (std::size_t i = 0; i < pattern.size(); i++)
            {
                str[pos + i] = pattern[i];
            }
        };

        for (std::size_t text_size = text_size_min; text_size < text_size_max; text_size += text_size_step)
        {
            profile_statistic result_for_text_size;
            result_for_text_size.text_size = text_size;

            for (std::size_t pattern_size = pattern_size_min;
               pattern_size < pattern_size_max;
               pattern_size += pattern_size_step)
            {   
                result_for_text_size.pattern_sizes.push_back(pattern_size);
                double total_time = 0;

                for (std::size_t iteration = 0; iteration < iterations_per_size_pair; iteration++)
                {
                    auto text = get_random_string(text_size);
                    const auto pattern = get_random_string(pattern_size);

                    std::uniform_int_distribution<> pattern_pos(0, static_cast<int>(text_size - pattern_size));
                    bool is_insert_pattern = pattern_occurrence_dist(gen);
                    if (is_insert_pattern)
                    {
                        insert_pattern(text, pattern, pattern_pos(gen));
                    }


                    std::size_t pos = 0;

                    while (pos < text_size)
                    {
                        {
                            ACCUMULATE_DURATION(total_time);
                            pos = algorithm(text, pattern, pos).first;                            
                        }

                        pos++;
                    }

                }

                double average_time = total_time / iterations_per_size_pair;
                result_for_text_size.time_for_pattern_size.push_back(average_time);
            }

            result.emplace_back(std::move(result_for_text_size));            
        }


        return result;
    }

    template <typename Algorithm>
    profile_statistic run_bencmark(Algorithm algorithm,
                                                const std::string& text,
                                                const std::string& pattern,
                                                std::size_t repeats                                 
    )
    {
        profile_statistic result;
        result.text_size = text.size();
        result.pattern_sizes = {pattern.size()};

        double total_time = 0;

        for (std::size_t i = 0; i < repeats; i++)
        {
            ACCUMULATE_DURATION(total_time);
            auto [pos, ops] = algorithm(text, pattern, 0);  
        }

        double average_time = total_time / repeats;
        result.time_for_pattern_size = {average_time};        
        result.operations = ops;

        return result;
    }

} // namespace profiler
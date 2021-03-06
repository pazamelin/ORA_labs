#include "str_match/all.hpp"

#include "debug.hpp"

#include <iostream>
#include <vector>
#include <utility>
#include <functional>
#include <random>

#define CATCH_CONFIG_MAIN
#define CATCH_CONFIG_ENABLE_BENCHMARKING
#include <catch2/catch.hpp>

template <typename AlgorithmLHS, typename AlgorithmRHS>
void stress_test(AlgorithmLHS algorithmLhs,
                 AlgorithmRHS algorithmRhs,
                 std::size_t text_size_min,
                 std::size_t text_size_max,
                 std::size_t text_size_step,
                 std::size_t iteration_per_size,
                 std::size_t pattern_size)
{
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
        for (std::size_t iteration = 0; iteration < iteration_per_size; iteration++)
        {
            auto text = get_random_string(text_size);
            const auto pattern = get_random_string(pattern_size);

            std::uniform_int_distribution<> pattern_pos(0, static_cast<int>(text_size - pattern_size));
            bool is_insert_pattern = pattern_occurrence_dist(gen);
            if (is_insert_pattern)
            {
                insert_pattern(text, pattern, pattern_pos(gen));
            }

            std::size_t pos_lhs = 0;
            std::size_t pos_rhs = 0;

            pos_lhs = algorithmLhs(text, pattern, pos_lhs).first;
            pos_rhs = algorithmRhs(text, pattern, pos_rhs).first;
            
            if (pos_lhs != pos_rhs)
            {
                debug_log("text:", text);
                debug_log("pattern:", pattern);
                debug_log("has inserted pattern:", is_insert_pattern);

                (pos_lhs == text_size) ? debug_log("     LHS did not find")
                                       : debug_log("     LHS found at:", pos_lhs);
                (pos_rhs == text_size) ? debug_log("     RHS did not find")
                                       : debug_log("     RHS found at:", pos_rhs);
              
                debug_log("");              
            }
          
            REQUIRE(pos_lhs == pos_rhs);          
        }
    }
}

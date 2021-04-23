#pragma once

#include <string>

namespace str_match
{

    namespace detail
    {
        std::size_t pow(std::size_t base, std::size_t exp);

        std::size_t rolling_hash(const std::string& str, std::size_t pos, std::size_t len);

        std::size_t roll_hash(const std::string& str, std::size_t pos, std::size_t len, std::size_t previous_hash);
    }


    std::size_t rabin_karp(const std::string& text, const std::string& pattern, std::size_t pos); 

}  // namespace str_match

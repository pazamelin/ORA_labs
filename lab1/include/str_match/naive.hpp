#pragma once

#include <string>

namespace str_match
{
    std::pair<std::size_t, std::size_t>
    naive(const std::string& text, const std::string& pattern, std::size_t pos);

}  // namespace str_match

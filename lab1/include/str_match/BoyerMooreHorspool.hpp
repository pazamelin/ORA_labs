#pragma once

#include <string>

namespace str_match
{
	std::size_t boyer_moore_horspool(const std::string& text, const std::string& pattern, std::size_t pos);

}  // namespace str_match

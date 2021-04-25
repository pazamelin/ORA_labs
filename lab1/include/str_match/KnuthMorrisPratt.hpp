#pragma once

#include <string>
#include <vector>

namespace str_match
{
	namespace detail
	{
		std::vector<std::size_t> prefix_function(const std::string& s);
	}

	std::pair<std::size_t, std::size_t>
	knuth_morris_pratt(const std::string& text, const std::string& pattern, std::size_t pos);

}  // namespace str_match

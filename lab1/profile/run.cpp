#include <iostream>
#include <fstream>
#include <string_view>
#include <vector>
#include <exception>
#include <sstream>
#include <string>
#include <set>

#include <str_match/all.hpp>

#include "profiler.hpp"


void write_csv(const std::string& csv_filename,
	const std::vector<profiler::profile_statistic>& result
)
{
	std::cout << csv_filename << std::endl;
	std::ofstream csv_file(csv_filename, std::ios::out | std::ios::trunc);
	if (csv_file.is_open())
	{

		csv_file << "text_size,";

		for (std::size_t i = 0; i < result[0].pattern_sizes.size(); i++)
		{
			csv_file << "pattern_size_" << i << ",";
			csv_file << "time_" << i;
			if (i < result[0].pattern_sizes.size() - 1)
			{
				csv_file << ",";
			}
			else
			{
				csv_file << "\n";
			}

		}

		for (const auto& statistic : result)
		{
			csv_file << statistic.text_size << ",";

			for (std::size_t i = 0; i < statistic.pattern_sizes.size(); i++)
			{
				csv_file << statistic.pattern_sizes[i] << ",";
				csv_file << statistic.time_for_pattern_size[i]; 

				if (i < result[0].pattern_sizes.size() - 1)
				{
					csv_file << ",";
				}
				else
				{
					csv_file << "\n";
				}

			}
		}
	}
	else
	{
		throw std::runtime_error("failed to open a file");
	}
}

void profile_all()
{
	using profiler::profile;

	std::size_t text_size_min = 100;
	std::size_t text_size_max = 10001;
	std::size_t text_size_step = 100;
	std::size_t pattern_size_min = 10;
	std::size_t pattern_size_max = 101;
	std::size_t pattern_size_step = 10;
	std::size_t iterations_per_size_pair = 10;   

	std::string filename_prefix = "../../../lab1/profile/results/";

	{   // NAIVE
		const auto results = profile(str_match::naive,
								 text_size_min,
								 text_size_max,
								 text_size_step,
								 pattern_size_min,
								 pattern_size_max,
								 pattern_size_step,
								 iterations_per_size_pair);

		write_csv(filename_prefix + "naive.csv", results);
	}

	{   // RABIN_KARP
		const auto results = profile(str_match::rabin_karp,
								 text_size_min,
								 text_size_max,
								 text_size_step,
								 pattern_size_min,
								 pattern_size_max,
								 pattern_size_step,
								 iterations_per_size_pair);

		write_csv(filename_prefix + "rabin_karp.csv", results);
	}	
}


int main(int argc, char* argv[])
{
	profile_all();
	return 0;
}
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

	{   // BOYER_MOORE_HORSPOOL
		const auto results = profile(str_match::boyer_moore_horspool,
								 text_size_min,
								 text_size_max,
								 text_size_step,
								 pattern_size_min,
								 pattern_size_max,
								 pattern_size_step,
								 iterations_per_size_pair);

		write_csv(filename_prefix + "BMH.csv", results);
	}	

	{   // KNUTH_MORRIS_PRATT
		const auto results = profile(str_match::knuth_morris_pratt,
								 text_size_min,
								 text_size_max,
								 text_size_step,
								 pattern_size_min,
								 pattern_size_max,
								 pattern_size_step,
								 iterations_per_size_pair);

		write_csv(filename_prefix + "KMP.csv", results);
	}
}

void run_benchmarks()
{
	std::string filename_prefix = "../../../lab1/profile/results/";
	std::string benchmarks_prefix = "../../../lab1/profile/benchmarks/";

	auto read_file = [](const std::string& filename)
	{
		std::ifstream csv_file(filename, std::ios::in);
		if (csv_file.is_open())
		{
			return std::string(std::istreambuf_iterator<char>(csv_file),
                 			   std::istreambuf_iterator<char>());
		}
		else
		{
			throw std::runtime_error("failed to open a file IN");
		}
	};

	std::vector<std::string> types = {"bad", "good"};
	std::vector<int> nums = {1, 2, 3, 4};

	std::ofstream csv_file(filename_prefix + "benchmarking.csv", std::ios::out | std::ios::trunc);
	if (!csv_file.is_open())
	{
		throw std::runtime_error("failed to open a file OUT");
	}

	csv_file << "benchmark, algorithm, time, operations\n";	 

	for (const auto& type : types)
	{
		for (int num : nums)
		{
			std::string filename_t = benchmarks_prefix + type + "_t_" + std::to_string(num) + ".txt";
			std::string filename_w = benchmarks_prefix + type + "_w_" + std::to_string(num) + ".txt";
			std::string text = read_file(filename_t);
			std::cout << "TEXT: " << text << std::endl;

			std::string pattern = read_file(filename_w);
			std::cout << "PATTERN: " << pattern << std::endl;			

			{   // NAIVE
				csv_file << type + "_" + std::to_string(num) << ",";

				auto result_1 = profiler::run_bencmark(str_match::naive,
													   text,
													   pattern, 10);
				csv_file << "naive," << result_1.time_for_pattern_size[0] << "," << result_1.operations << "\n";	
			}

			{   // RABIN_KARP
				csv_file << type + "_" + std::to_string(num) << ",";

				auto result_1 = profiler::run_bencmark(str_match::rabin_karp,
													   text,
													   pattern, 10);
				csv_file << "rabin_karp," << result_1.time_for_pattern_size[0]<< "," << result_1.operations << "\n";	
			}

			
			{   // BMH
				csv_file << type + "_" + std::to_string(num) << ",";

				auto result_1 = profiler::run_bencmark(str_match::boyer_moore_horspool,
													   text,
													   pattern, 10);
				csv_file << "BMH," << result_1.time_for_pattern_size[0] << "," << result_1.operations << "\n";	
			}

			
			{   // KMP
				csv_file << type + "_" + std::to_string(num) << ",";

				auto result_1 = profiler::run_bencmark(str_match::knuth_morris_pratt,
													   text,
													   pattern, 10);
				csv_file << "KMP," << result_1.time_for_pattern_size[0] << "," << result_1.operations << "\n";
			}
			
		}
	}
	

}

int main(int argc, char* argv[])
{
	//profile_all();
	run_benchmarks();
	return 0;
}
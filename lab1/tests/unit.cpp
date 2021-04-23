#include "templates.hpp"

TEST_CASE("rabin-karp 1", "[unit]")
{
    const std::string text = "afuua";
    const std::string pattern = "fuu";

    std::size_t pos = str_match::rabin_karp(text, pattern, 0);
    REQUIRE(pos == 1);
}

TEST_CASE("rabin-karp 2", "[unit]")
{
    const std::string text = "sdfuusggfuux";
    const std::string pattern = "fuu";

    std::size_t pos = 0;
    pos = str_match::rabin_karp(text, pattern, pos);
    REQUIRE(pos == 2);

    pos = str_match::rabin_karp(text, pattern, pos + 3);
    REQUIRE(pos == 8);
}
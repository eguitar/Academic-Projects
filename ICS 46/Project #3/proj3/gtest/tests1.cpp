#include "gtest/gtest.h"
#include "Wordset.hpp"
#include "convert.hpp"
#include "ver.hpp"
#include <string>
#include <fstream>

namespace{


// NOTE:  these are not intended as exhaustive tests.
// This should get you started testing.
// You MAY use validConversion in unit tests (i.e., this file and any other unit tests in this folder you add),
// but you MAY NOT use it in your code otherwise. 

TEST(HashFunctionTest, Hf1)
{
	unsigned hv = polynomialHashFunction("dbc", 37, 100000);
	unsigned shouldBe = 4*37*37 + 2*37 + 3;
	EXPECT_EQ(hv, shouldBe);
}

TEST(HashFunctionTest, Hf2)
{
	unsigned hv = polynomialHashFunction("abcdef", 2, 100000);
	unsigned shouldBe = 6*1+5*2+4*2*2+3*2*2*2+2*2*2*2*2+1*2*2*2*2*2;
	EXPECT_EQ(hv, shouldBe);
}

TEST(HashFunctionTest, Hf3)
{
	unsigned hv = polynomialHashFunction("fedcba", 2, 100000);
	unsigned shouldBe = 1+2*2+3*2*2+4*2*2*2+5*2*2*2*2+6*2*2*2*2*2;
	EXPECT_EQ(hv, shouldBe);
}

TEST(HashFunctionTest, Hf4)
{
	unsigned hv = polynomialHashFunction("abcdef", 37, 100000);
	unsigned shouldBe = 6*1+5*37+4*37*37+3*37*37*37+2*37*37*37*37+1*37*37*37*37*37;
	shouldBe = shouldBe % 100000;
	EXPECT_EQ(hv, shouldBe);
}

TEST(HashFunctionTest, Hf5)
{
	unsigned hv = polynomialHashFunction("fedcba", 37, 100000);
	unsigned shouldBe = 1+2*37+3*37*37+4*37*37*37+5*37*37*37*37+6*37*37*37*37*37;
	shouldBe = shouldBe % 100000;
	EXPECT_EQ(hv, shouldBe);
}

TEST(HashFunctionTest, Hf6)
{
	unsigned hv = polynomialHashFunction("abcdef", 100, 10);
	unsigned shouldBe = 10203040506 % 10;
	EXPECT_EQ(hv, shouldBe);
}

TEST(HashFunctionTest, Hf7)
{
	unsigned hv = polynomialHashFunction("fedcba", 100, 10);
	unsigned shouldBe = 60504030201 % 10;
	EXPECT_EQ(hv, shouldBe);
}


TEST(TableTest, Tab1)
{
	WordSet ws(11);
	ws.insert("dbc");
	EXPECT_TRUE(ws.contains("dbc"));
	EXPECT_EQ(ws.getCapacity(), 11);
}

TEST(ResizeTest, Tab2)
{
	WordSet ws(11);
	ws.insert("sleepy");
	ws.insert("happy");
	ws.insert("dopey");
	ws.insert("sneezy");
	ws.insert("datalink");
	ws.insert("australia");
	ws.insert("guacamole");
	ws.insert("phylum");
	EXPECT_TRUE(ws.contains("happy"));
	EXPECT_TRUE(ws.contains("dopey"));
	EXPECT_EQ(ws.getCapacity(), 11);
}

TEST(ResizeTest, Tab3)
{
	WordSet ws(11);
	ws.insert("sleepy");
	ws.insert("happy");
	ws.insert("dopey");
	ws.insert("sneezy");
	ws.insert("datalink");
	ws.insert("australia");
	ws.insert("guacamole");
	ws.insert("phylum");
	EXPECT_TRUE(ws.contains("happy"));
	EXPECT_TRUE(ws.contains("dopey"));
	ws.insert("salsa");
	ws.insert("sloth");
	ws.insert("colossus");
	ws.insert("synergize");
	ws.insert("monday");
	ws.insert("tuesday");
	ws.insert("wednesday");
	ws.insert("thursday");
	ws.insert("friday");
	ws.insert("saturday");
	ws.insert("sunday");
	EXPECT_TRUE(ws.contains("monday"));
	EXPECT_TRUE(ws.contains("sunday"));
	EXPECT_EQ(ws.getCapacity(), 23);
}


TEST(ConvertWords, AntToArt)
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);

 	std::vector< std::string > r  = convert("ant", "art", words);

 	// this was a success if r was a valid conversion of length 2.
	std::ifstream in2("words.txt");
 	EXPECT_EQ(r.size(), 2);
 	EXPECT_TRUE(  validConversion(r, "ant", "art", in2) );
}



TEST(ConvertWords, AntToEat)
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);

 	std::vector< std::string > r = convert("ant", "eat", words);

	std::ifstream in2("words.txt");

 	EXPECT_EQ(r.size(), 5);
 	EXPECT_TRUE(  validConversion(r, "ant", "eat", in2) );
}

TEST(ConvertWords, ColdToWarm)
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);

 	std::vector< std::string > r = convert("cold", "warm", words);

	std::ifstream in2("words.txt");

 	EXPECT_EQ(r.size(), 5);
 	EXPECT_TRUE(  validConversion(r, "cold", "warm", in2) );
}

TEST(ConvertWords, ChangeToComedo)
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);

 	std::vector< std::string > r = convert("change", "comedo", words);

	std::ifstream in2("words.txt");

 	EXPECT_EQ(r.size(), 0);
 	EXPECT_FALSE(  validConversion(r, "change", "comedo", in2) );
}

TEST(ConvertWords, AbilitiesToSeventeen)
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);

 	std::vector< std::string > r = convert("abilities", "seventeen", words);

	std::ifstream in2("words.txt");

 	EXPECT_EQ(r.size(), 0);
 	EXPECT_FALSE(  validConversion(r, "abilities", "seventeen", in2) );
}

TEST(ConvertWords, AbilitiesToAbilities)
{
	WordSet words(11);
	std::ifstream in("words.txt");
	loadWordsIntoTable(words, in);

 	std::vector< std::string > r = convert("abilities", "abilities", words);

	std::ifstream in2("words.txt");

 	EXPECT_EQ(r.size(), 2);
 	EXPECT_FALSE(  validConversion(r, "abilities", "abilities", in2) );
}


}
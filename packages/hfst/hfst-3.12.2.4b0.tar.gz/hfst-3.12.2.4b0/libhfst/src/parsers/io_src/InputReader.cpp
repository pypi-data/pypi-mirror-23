//! @file InputReader.cc
//!
//! @author Miikka Silfverberg

//   This program is free software: you can redistribute it and/or modify
//   it under the terms of the GNU General Public License as published by
//   the Free Software Foundation, version 3 of the Licence.
//
//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//   GNU General Public License for more details.
//
//   You should have received a copy of the GNU General Public License
//   along with this program.  If not, see <http://www.gnu.org/licenses/>.

#include "InputReader.h"

InputReader::InputReader(size_t &counter):
  input_stream(NULL),
  counter(counter),
  buffer_size(500000),
  buffer_index(0),
  warning_stream(NULL),
  error_stream(NULL)
{}

void InputReader::reset()
{
  input_stream = NULL;
  // counter is a reference, so it must be reset separately
  buffer_size = 500000;
  buffer_index = 0;
  warning_stream = NULL;
  error_stream = NULL;
}

void InputReader::set_input(std::istream &file)
{
  input_stream = &file;
  input_stream->getline(buffer,buffer_size);
}

void InputReader::set_warning_stream(std::ostream & ostr)
{
  warning_stream = &ostr;
}

void InputReader::set_error_stream(std::ostream & ostr)
{
  error_stream = &ostr;
}

void InputReader::warn(const std::string &warning)
{
  if (warning_stream != NULL)
    {
      *warning_stream << std::endl;
      *warning_stream << warning << std::endl;
      *warning_stream << "on line " << counter << ":" << std::endl;
      *warning_stream << buffer << std::endl;
    }
}

void InputReader::error(const std::string &err)
{
  if (error_stream != NULL)
    {
      *error_stream << std::endl;
      *error_stream << err << std::endl;
      *error_stream << "on line " << counter << ":" << std::endl;
      *error_stream << buffer << std::endl;
      *error_stream << "Aborted." << std::endl << std::endl;
    }
}

char InputReader::input(void)
{
  if (input_stream == NULL)
    { throw InputNotSet(); }
  if (buffer[buffer_index] == 0)
    {
      input_stream->getline(buffer,buffer_size);
      if (input_stream->gcount() == 0)
    { return 0; }
      buffer_index = 0;
      return '\n';
    }
  return buffer[buffer_index++];
}

#ifdef INPUT_READER_TEST
#include <sstream>
#include <cassert>
int main(void)
{
  std::string str1
    ("Some text spanning one line only.");
  std::istringstream in1(str1);
  size_t counter = 1;
  InputReader ir1(counter);
  try
    {
      ir1.input();
      assert(false);
    }
  catch (const InputNotSet &e)
    { /* nothing */ }
  ir1.set_input(in1);
  assert(ir1.input() == 'S');
  assert(ir1.input() == 'o');
  assert(ir1.input() == 'm');
  assert(ir1.input() == 'e');
  assert(ir1.input() == ' ');
  assert(ir1.input() == 't');
  assert(ir1.input() == 'e');
  assert(ir1.input() == 'x');
  assert(ir1.input() == 't');
  assert(ir1.input() == ' ');
  assert(ir1.input() == 's');
  assert(ir1.input() == 'p');
  assert(ir1.input() == 'a');
  assert(ir1.input() == 'n');
  assert(ir1.input() == 'n');
  assert(ir1.input() == 'i');
  assert(ir1.input() == 'n');
  assert(ir1.input() == 'g');
  assert(ir1.input() == ' ');
  assert(ir1.input() == 'o');
  assert(ir1.input() == 'n');
  assert(ir1.input() == 'e');
  assert(ir1.input() == ' ');
  assert(ir1.input() == 'l');
  assert(ir1.input() == 'i');
  assert(ir1.input() == 'n');
  assert(ir1.input() == 'e');
  assert(ir1.input() == ' ');
  assert(ir1.input() == 'o');
  assert(ir1.input() == 'n');
  assert(ir1.input() == 'l');
  assert(ir1.input() == 'y');
  assert(ir1.input() == '.');
  assert(ir1.input() == 0);

  std::string str2
    ("line\nline.");
  std::istringstream in2(str2);
  InputReader ir2(counter);
  ir2.set_input(in2);
  assert(ir2.input() == 'l');
  assert(ir2.input() == 'i');
  assert(ir2.input() == 'n');
  assert(ir2.input() == 'e');
  assert(ir2.input() == '\n');
  assert(ir2.input() == 'l');
  assert(ir2.input() == 'i');
  assert(ir2.input() == 'n');
  assert(ir2.input() == 'e');
  assert(ir2.input() == '.');
  assert(ir2.input() == 0);
  assert(ir2.input() == 0);
}
#endif

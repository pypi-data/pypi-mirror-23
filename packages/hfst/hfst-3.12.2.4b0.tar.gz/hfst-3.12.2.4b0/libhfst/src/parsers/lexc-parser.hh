/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_HLEXC_LEXC_PARSER_HH_INCLUDED
# define YY_HLEXC_LEXC_PARSER_HH_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int hlexcdebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    ERROR = 258,
    MULTICHARS_START = 259,
    DEFINITIONS_START = 260,
    END_START = 261,
    NOFLAGS_START = 262,
    LEXICON_START = 263,
    LEXICON_START_WRONG_CASE = 264,
    LEXICON_NAME = 265,
    ULSTRING = 266,
    ENTRY_GLOSS = 267,
    MULTICHAR_SYMBOL = 268,
    DEFINITION_NAME = 269,
    DEFINITION_EXPRESSION = 270,
    XEROX_REGEXP = 271
  };
#endif
/* Tokens.  */
#define ERROR 258
#define MULTICHARS_START 259
#define DEFINITIONS_START 260
#define END_START 261
#define NOFLAGS_START 262
#define LEXICON_START 263
#define LEXICON_START_WRONG_CASE 264
#define LEXICON_NAME 265
#define ULSTRING 266
#define ENTRY_GLOSS 267
#define MULTICHAR_SYMBOL 268
#define DEFINITION_NAME 269
#define DEFINITION_EXPRESSION 270
#define XEROX_REGEXP 271

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 207 "lexc-parser.yy" /* yacc.c:1909  */

    char* name;
    int number;

#line 91 "lexc-parser.hh" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE YYLTYPE;
struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif


extern YYSTYPE hlexclval;
extern YYLTYPE hlexclloc;
int hlexcparse (void);

#endif /* !YY_HLEXC_LEXC_PARSER_HH_INCLUDED  */

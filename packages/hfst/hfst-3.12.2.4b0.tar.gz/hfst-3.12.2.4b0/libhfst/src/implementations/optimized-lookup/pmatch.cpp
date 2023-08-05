// Copyright (c) 2016 University of Helsinki
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 3 of the License, or (at your option) any later version.
// See the file COPYING included with this distribution for more
// information.
#include "pmatch.h"
#include "hfst.h"

using hfst::HfstTransducer;

namespace hfst_ol {

PmatchAlphabet::PmatchAlphabet(std::istream & inputstream,
                               SymbolNumber symbol_count,
                               PmatchContainer * cont):
    TransducerAlphabet(inputstream, symbol_count, false),
    special_symbols(SPECIALSYMBOL_NR_ITEMS, NO_SYMBOL_NUMBER), // SpecialSymbols enum
    container(cont)
{
    symbol2lists = SymbolNumberVector(orig_symbol_count, NO_SYMBOL_NUMBER);
    list2symbols = SymbolNumberVector(orig_symbol_count, NO_SYMBOL_NUMBER);
    rtns = RtnVector(orig_symbol_count, NULL);
    // We initialize the vector of which symbols have a printable representation
    // with false, then flip those that actually do to true
    printable_vector = std::vector<bool>(orig_symbol_count, false);
    for (SymbolNumber i = 1; i < symbol_table.size(); ++i) {
        if (is_special(symbol_table[i])) {
            add_special_symbol(symbol_table[i], i);
        } else {
            if (!is_flag_diacritic(i)) {
                printable_vector[i] = true;
            }
        }
    }
}

PmatchAlphabet::PmatchAlphabet(TransducerAlphabet const & a,
                               PmatchContainer * cont):
    TransducerAlphabet(a),
    special_symbols(SPECIALSYMBOL_NR_ITEMS, NO_SYMBOL_NUMBER),
    container(cont) {
    symbol2lists = SymbolNumberVector(orig_symbol_count, NO_SYMBOL_NUMBER);
    list2symbols = SymbolNumberVector(orig_symbol_count, NO_SYMBOL_NUMBER);
    rtns = RtnVector(orig_symbol_count, NULL);
    // We initialize the vector of which symbols have a printable representation
    // with false, then flip those that actually do to true
    printable_vector = std::vector<bool>(orig_symbol_count, false);
    for (SymbolNumber i = 1; i < symbol_table.size(); ++i) {
        if (is_special(symbol_table[i])) {
            add_special_symbol(symbol_table[i], i);
        } else {
            if (!is_flag_diacritic(i)) {
                printable_vector[i] = true;
            }
        }
    }
}

PmatchAlphabet::PmatchAlphabet(void):
    TransducerAlphabet()
{}

void PmatchAlphabet::add_symbol(const std::string & symbol)
{
    symbol2lists.push_back(NO_SYMBOL_NUMBER);
    list2symbols.push_back(NO_SYMBOL_NUMBER);
    rtns.push_back(NULL);
    printable_vector.push_back(true);
    if (exclusionary_lists.size() != 0) {
        // if there are exclusionary lists, they should all accept the new symbol
        symbol2lists[symbol_table.size()] = hfst::size_t_to_ushort(symbol_lists.size());
        symbol_lists.push_back(SymbolNumberVector(exclusionary_lists.begin(),
                                                  exclusionary_lists.end()));
#if defined(_MSC_VER) || defined(NO_CPLUSPLUS_11)
        for (SymbolNumberVector::const_iterator exc = exclusionary_lists.begin(); exc != exclusionary_lists.end(); exc++) {
          symbol_list_members[list2symbols[*exc]].push_back(hfst::size_t_to_uint(symbol_table.size()));
        }
#else
	for(const auto & exc: exclusionary_lists) {
          symbol_list_members[list2symbols[exc]].push_back(symbol_table.size());
        }
#endif
    }
    TransducerAlphabet::add_symbol(symbol);
}

bool PmatchAlphabet::is_printable(SymbolNumber symbol)
{
    return symbol < printable_vector.size() && printable_vector[symbol];
}

void PmatchAlphabet::add_special_symbol(const std::string & str,
                                         SymbolNumber symbol_number)
{
    if (str == "@PMATCH_ENTRY@") {
        special_symbols[entry] = symbol_number;
    } else if (str == "@PMATCH_EXIT@") {
        special_symbols[exit] = symbol_number;
    } else if (str == "@PMATCH_LC_ENTRY@") {
        special_symbols[LC_entry] = symbol_number;
    } else if (str == "@PMATCH_RC_ENTRY@") {
        special_symbols[RC_entry] = symbol_number;
    } else if (str == "@PMATCH_LC_EXIT@") {
        special_symbols[LC_exit] = symbol_number;
    } else if (str == "@PMATCH_RC_EXIT@") {
        special_symbols[RC_exit] = symbol_number;
    } else if (str == "@PMATCH_NLC_ENTRY@") {
        special_symbols[NLC_entry] = symbol_number;
    } else if (str == "@PMATCH_NRC_ENTRY@") {
        special_symbols[NRC_entry] = symbol_number;
    } else if (str == "@PMATCH_NLC_EXIT@") {
        special_symbols[NLC_exit] = symbol_number;
    } else if (str == "@PMATCH_NRC_EXIT@") {
        special_symbols[NRC_exit] = symbol_number;
    } else if (str == "@PMATCH_PASSTHROUGH@") {
        special_symbols[Pmatch_passthrough] = symbol_number;
    } else if (str == "@PMATCH_INPUT_MARK@") {
        special_symbols[Pmatch_input_mark] = symbol_number;
    } else if (str == "@BOUNDARY@") {
        special_symbols[boundary] = symbol_number;
    } else if (is_end_tag(str)) {
        // Fetch the part between @PMATCH_ENDTAG_ and @
        end_tag_map[symbol_number] = str.substr(
            sizeof("@PMATCH_ENDTAG_") - 1,
            str.size() - (sizeof("@PMATCH_ENDTAG_@") - 1));
    } else if (is_capture_tag(str)) {
        capture_tag_map[symbol_number] = str.substr(
            sizeof("@PMATCH_CAPTURE_") - 1,
            str.size() - (sizeof("@PMATCH_CAPTURE_@") - 1));
    } else if (is_captured_tag(str)) {
        captured_tag_map[symbol_number] = str.substr(
            sizeof("@PMATCH_CAPTURED_") - 1,
            str.size() - (sizeof("@PMATCH_CAPTURED_@") - 1));
    } else if (is_insertion(str)) {
        rtn_names[name_from_insertion(str)] = symbol_number;
    } else if (is_guard(str)) {
        guards.push_back(symbol_number);
    } else if (is_list(str)) {
        process_symbol_list(str, symbol_number);
    } else if (is_counter(str)) {
        process_counter(str, symbol_number);
    } else {
        printable_vector[symbol_number] = true;
        // it's a regular symbol, we shouldn't be here!
//        std::cerr << "pmatch: warning: symbol " << str << " was wrongly given as a special symbol\n";
    }
}

void PmatchAlphabet::process_symbol_list(std::string str, SymbolNumber sym)
{
    SymbolNumberVector list_symbols;
    StringSymbolMap ss = build_string_symbol_map();
    // regular list or exlusionary list?
    bool polarity = str[1] == 'L';
    size_t begin = strlen("@L.");
    size_t stop;
    std::vector<std::string> collected_symbols;
    while ((stop = str.find('_', begin)) != std::string::npos) {
// For each underscore after the prelude, grab the substring
        std::string symbol = str.substr(begin, stop - begin);
        if (symbol.size() == 0) {
// If the symbol _is_ an underscore it looks like we got an empty string
            symbol = "_";
            begin = stop + 2;
        } else {
            begin = stop + 1;
        }
        collected_symbols.push_back(symbol);
    }
    // Process the symbols we found
    for (std::vector<std::string>::const_iterator it = collected_symbols.begin();
         it != collected_symbols.end(); ++it) {
        SymbolNumber str_sym;
        if (ss.count(*it) == 0) {
// This symbol isn't mentioned elsewhere in the alphabet
            add_symbol(*it);
            str_sym = orig_symbol_count;
            ++orig_symbol_count;
        } else {
            str_sym = ss[*it];
        }
        list_symbols.push_back(str_sym);
        if (polarity == true) {
            if (symbol2lists[str_sym] == NO_SYMBOL_NUMBER) {
              symbol2lists[str_sym] = hfst::size_t_to_ushort(symbol_lists.size());
                symbol_lists.push_back(SymbolNumberVector(1, sym));
            } else {
                symbol_lists[symbol2lists[str_sym]].push_back(sym);
            }
        }
    }
    list2symbols[sym] = hfst::size_t_to_ushort(symbol_list_members.size());
    if (polarity == false) {
        SymbolNumberVector excl_symbols;
        exclusionary_lists.push_back(sym);
        for (SymbolNumber candidate_for_list = 1; candidate_for_list < symbol_table.size(); ++candidate_for_list) {
            if (is_printable(symbol_table[candidate_for_list]) &&
                find(list_symbols.begin(), list_symbols.end(), candidate_for_list) == list_symbols.end()) {
                excl_symbols.push_back(candidate_for_list);
                if (symbol2lists[candidate_for_list] == NO_SYMBOL_NUMBER) {
                  symbol2lists[candidate_for_list] = hfst::size_t_to_ushort(symbol_lists.size());
                    symbol_lists.push_back(SymbolNumberVector(1, sym));
                } else {
                    symbol_lists[symbol2lists[sym]].push_back(sym);
                }
            }
        }
        symbol_list_members.push_back(excl_symbols);
    } else {
        symbol_list_members.push_back(list_symbols);
    }
}

SymbolNumberVector PmatchAlphabet::get_specials(void) const
{
    SymbolNumberVector v;
    for (SymbolNumberVector::const_iterator it =
             special_symbols.begin(); it != special_symbols.end(); ++it) {
        if (*it != NO_SYMBOL_NUMBER) {
            v.push_back(*it);
        }
    }
    return v;
}

void PmatchAlphabet::process_counter(std::string str, SymbolNumber sym)
{
    // Fill up non-counter spots in the counter vector with blanks
    while (counters.size() < sym) {
        counters.push_back(NO_COUNTER);
    }
    counters.push_back(0);
}

void PmatchAlphabet::count(SymbolNumber sym)
{
    if (is_counter(sym)) {
        counters[sym]++;
    }
}

void PmatchContainer::collect_first_symbols(void)
{
    // Fetch the first symbols from any
    // first-position rtn arcs in TOP. If they are potential epsilon loops,
    // clear out the set.
    toplevel->collect_possible_first_symbols();

    SymbolNumber max_input_sym = 0;
    std::set<SymbolNumber> & possible_firsts = toplevel->possible_first_symbols;
    for (std::set<SymbolNumber>::iterator it = possible_firsts.begin();
         it != possible_firsts.end(); ++it) {
        if (*it > max_input_sym) { max_input_sym = *it; }
        if (alphabet.has_rtn(*it)) {
            if (alphabet.get_rtn(*it) == toplevel) {
                possible_firsts.clear();
                break;
            }
            alphabet.get_rtn(*it)->collect_possible_first_symbols();
            std::set<SymbolNumber> rtn_firsts =
                alphabet.get_rtn(*it)->possible_first_symbols;
            for (RtnNameMap::const_iterator it = alphabet.rtn_names.begin();
                 it != alphabet.rtn_names.end(); ++it) {
                if (rtn_firsts.count(it->second) == 1) {
                    // For now we are very conservative:
                    // if we can go through two levels of rtns
                    // without any input, we just assume the full
                    // input set is possible
                    possible_firsts.clear();
                }
            }
            if (rtn_firsts.empty() || possible_firsts.empty()) {
                possible_firsts.clear();
                break;
            } else {
                for (std::set<SymbolNumber>::
                         const_iterator rtn_it = rtn_firsts.begin();
                     rtn_it != rtn_firsts.end(); ++rtn_it) {
                    if (*rtn_it > max_input_sym) { max_input_sym = *rtn_it ;}
                    possible_firsts.insert(*rtn_it);
                }
            }
        }
    }
    for (RtnNameMap::const_iterator it = alphabet.rtn_names.begin();
         it != alphabet.rtn_names.end(); ++it) {
        possible_firsts.erase(it->second);
    }
    if (!possible_firsts.empty() &&
        alphabet.get_special(boundary) != NO_SYMBOL_NUMBER) {
        possible_firsts.insert(alphabet.get_special(boundary));
    }
    if (!possible_firsts.empty()) {
        for (int i = 0; i <= max_input_sym; ++i) {
            if (possible_firsts.count(i) == 1) {
                possible_first_symbols.push_back(1);
            } else {
                possible_first_symbols.push_back(0);
            }
        }
    }
}

PmatchContainer::PmatchContainer(std::istream & inputstream):
    entry_stack(),
    verbose(false),
    locate_mode(false),
    line_number(0),
    profile_mode(false),
    single_codepoint_tokenization(false),
    running_weight(0.0)
{
    set_properties();
    reset_recursion();
    std::string transducer_name;
    std::map<std::string, std::string> properties = parse_hfst3_header(inputstream);
    if (properties.count("name") == 0) {
        std::cerr << "pmatch: warning: TOP not defined in archive, using first as TOP\n";
        transducer_name = "TOP";
    } else {
        transducer_name = properties["name"];
        if (transducer_name != "TOP") {
            std::cerr << "pmatch: warning: TOP not defined in archive, using first as TOP\n";
        }
    }
    if (properties.count("type") == 0) {
        std::cerr << "pmatch: warning: type information missing from archive\n";
    } else {
        if (properties["type"] != "HFST_OLW") {
            std::cerr << "pmatch: warning: archive type isn't weighted optimized-lookup according to header\n";
        }
    }
    set_properties(properties);
    TransducerHeader header(inputstream);
    alphabet = PmatchAlphabet(inputstream, header.symbol_count(), this);
    orig_symbol_count = symbol_count = alphabet.get_orig_symbol_count();
    encoder = new Encoder(alphabet.get_symbol_table(), orig_symbol_count);
    toplevel = new hfst_ol::PmatchTransducer(
        inputstream,
        header.index_table_size(),
        header.target_table_size(),
        alphabet,
        "TOP",
        this);
    while (inputstream.good()) {
        try {
            properties = parse_hfst3_header(inputstream);
            transducer_name = properties["name"];
        } catch (TransducerHeaderException & e) {
          (void)e; break;
        }
        header = TransducerHeader(inputstream);
        TransducerAlphabet dummy = TransducerAlphabet(
            inputstream, header.symbol_count());
        hfst_ol::PmatchTransducer * rtn =
            new hfst_ol::PmatchTransducer(inputstream,
                                          header.index_table_size(),
                                          header.target_table_size(),
                                          alphabet,
                                          transducer_name,
                                          this);
        if (!alphabet.has_rtn(transducer_name)) {
            alphabet.add_rtn(rtn, transducer_name);
        } else {
            delete rtn;
        }
    }
    collect_first_symbols();
}

PmatchContainer::PmatchContainer(Transducer * t):
    entry_stack(),
    verbose(false),
    locate_mode(false),
    profile_mode(false),
    single_codepoint_tokenization(false),
    running_weight(0.0)
{
    set_properties();
    reset_recursion();
    //TransducerHeader header = t->get_header();
    alphabet = PmatchAlphabet(t->get_alphabet(), this);
    orig_symbol_count = symbol_count = alphabet.get_orig_symbol_count();
    line_number = 0;
    encoder = new Encoder(alphabet.get_symbol_table(), orig_symbol_count);
    TransducerTable<TransitionW> transitions = t->copy_transitionw_table();
    TransducerTable<TransitionWIndex> indices = t->copy_windex_table();
    toplevel = new hfst_ol::PmatchTransducer(
        transitions.get_vector(),
        indices.get_vector(),
        alphabet,
        "TOP",
        this);
    collect_first_symbols();
}

// This constructor handles all the awkward optimized-lookup specific
// harmonization, for which the conversion needs to be done anyway,
// so there's no advantage to passing it transducers in optimized-lookup
// format.
PmatchContainer::PmatchContainer(std::vector<HfstTransducer> transducers):
    entry_stack(),
    verbose(false),
    locate_mode(false),
    line_number(0),
    profile_mode(false),
    single_codepoint_tokenization(false),
    running_weight(0.0)
{
    set_properties();
    reset_recursion();
    if (transducers.size() == 0) {
        return;
    }
    std::map<std::string, std::string> properties = transducers[0].get_properties();
    set_properties(properties);
    if (transducers.size() == 1) {
        HfstTransducer * top = NULL;
        if (transducers[0].get_type() != hfst::HFST_OLW_TYPE) {
            top = new HfstTransducer(transducers[0]);
            top->convert(hfst::HFST_OLW_TYPE);
        } else {
            top = &(transducers[0]);
        }
        Transducer * backend = hfst::implementations::ConversionFunctions::
            hfst_transducer_to_hfst_ol(top);
        TransducerHeader header(backend->get_header());
        alphabet = PmatchAlphabet(backend->get_alphabet(), this);
        orig_symbol_count = symbol_count = alphabet.get_orig_symbol_count();
        encoder = new Encoder(alphabet.get_symbol_table(), orig_symbol_count);
        TransducerTable<TransitionW> transitions = backend->copy_transitionw_table();
        TransducerTable<TransitionWIndex> indices = backend->copy_windex_table();
        toplevel = new hfst_ol::PmatchTransducer(
            transitions.get_vector(),
            indices.get_vector(),
            alphabet,
            "TOP",
            this);
        if (transducers[0].get_type() != hfst::HFST_OLW_TYPE) {
            // clean up if we needed a temp transducer
            delete top;
        }
    } else {
        // This is the difficult case where we have to make sure multiple
        // optimized-lookup transducers are harmonized with each other.

        HfstTransducer * top = NULL;
        std::vector<HfstTransducer *> temporaries(transducers.size(), NULL);
        // A dummy transducer with an alphabet with all the symbols
        HfstTransducer harmonizer(hfst::TROPICAL_OPENFST_TYPE);
        // First we need to collect a unified alphabet from all the transducers.
        hfst::StringSet symbols_seen;
        // We collect all the symbols and also copy and convert any non-olw bits
        for (size_t i = 0; i < transducers.size(); ++i) {
            hfst::StringSet string_set = transducers[i].get_alphabet();
            for (hfst::StringSet::const_iterator sym = string_set.begin();
                 sym != string_set.end(); ++sym) {
                if (symbols_seen.count(*sym) == 0) {
                    harmonizer.disjunct(HfstTransducer(*sym, harmonizer.get_type()));
                    symbols_seen.insert(*sym);
                }
            }
            if (transducers[i].get_name() == "TOP") {
                if (transducers[i].get_type() == hfst::HFST_OLW_TYPE) {
                top = &(transducers[i]);
                } else {
                    top = new HfstTransducer(transducers[i]);
                    top->convert(hfst::HFST_OLW_TYPE);
                }
            } else {
                if (transducers[i].get_type() == hfst::HFST_OLW_TYPE) {
                    temporaries[i] = &(transducers[i]);
                } else {
                    temporaries[i] = new HfstTransducer(transducers[i]);
                    (temporaries[i])->convert(hfst::HFST_OLW_TYPE);
                }
            }
        }
        if (top == NULL) {
            std::cerr << "pmatch: warning: TOP not defined in archive, using first as TOP\n";
            top = temporaries[0];
        }
        // Then we convert the harmonizer...
        harmonizer.convert(hfst::HFST_OLW_TYPE);
        // Use these for naughty intermediate steps to make sure
        // everything has the same alphabet
        hfst::HfstBasicTransducer * intermediate_tmp;
        hfst_ol::Transducer * harmonized_tmp;

        // We take care of TOP first
        intermediate_tmp = hfst::implementations::ConversionFunctions::
            hfst_transducer_to_hfst_basic_transducer(*top);
        harmonized_tmp = hfst::implementations::ConversionFunctions::
            hfst_basic_transducer_to_hfst_ol(intermediate_tmp,
                                             true, // weighted
                                             "", // no special options
                                             &harmonizer); // harmonize with this
        //TransducerHeader header = harmonized_tmp->get_header();
        // this will be the alphabet of the entire container
        alphabet = PmatchAlphabet(harmonized_tmp->get_alphabet(), this);
        orig_symbol_count = symbol_count = alphabet.get_orig_symbol_count();
        encoder = new Encoder(alphabet.get_symbol_table(), orig_symbol_count);
        TransducerTable<TransitionW> transitions = harmonized_tmp->copy_transitionw_table();
        TransducerTable<TransitionWIndex> indices = harmonized_tmp->copy_windex_table();
        toplevel = new hfst_ol::PmatchTransducer(
            transitions.get_vector(),
            indices.get_vector(),
            alphabet,
            "TOP",
            this);
        // Then we do the same for the other transducers except without
        // alphabets or encoders because those should be identical
        for (size_t i = 0; i < temporaries.size(); ++i) {
            if (temporaries[i] != NULL) {
                // there's a NULL where TOP should be
                intermediate_tmp = hfst::implementations::ConversionFunctions::
                    hfst_transducer_to_hfst_basic_transducer(*(temporaries[i]));
                harmonized_tmp = hfst::implementations::ConversionFunctions::
                    hfst_basic_transducer_to_hfst_ol(intermediate_tmp,
                                                     true, // weighted
                                                     "", // no special options
                                                     &harmonizer); // harmonize with this
                TransducerTable<TransitionW> transitions = harmonized_tmp->copy_transitionw_table();
                TransducerTable<TransitionWIndex> indices = harmonized_tmp->copy_windex_table();
                PmatchTransducer * rtn = new hfst_ol::PmatchTransducer(
                    transitions.get_vector(),
                    indices.get_vector(),
                    alphabet,
                    temporaries[i]->get_name(),
                    this);
                alphabet.add_rtn(rtn, temporaries[i]->get_name());
            }
        }
        // clean up the temporaries
        for (size_t i = 0; i < transducers.size(); ++i) {
            if (transducers[i].get_name() == "TOP") {
                if (transducers[i].get_type() != hfst::HFST_OLW_TYPE) {
                    delete top;
                }
            } else {
                if (transducers[i].get_type() != hfst::HFST_OLW_TYPE) {
                    delete temporaries[i];
                }
            }
        }
    }
    collect_first_symbols();
}

void PmatchContainer::add_rtn(Transducer * rtn, const std::string & name)
{
    TransducerTable<TransitionW> transitions = rtn->copy_transitionw_table();
    TransducerTable<TransitionWIndex> indices = rtn->copy_windex_table();
    PmatchTransducer * pmatch_rtn = new hfst_ol::PmatchTransducer(
        transitions.get_vector(),
        indices.get_vector(),
        alphabet,
        name,
        this);
    if (!alphabet.has_rtn(name)) {
        alphabet.add_rtn(pmatch_rtn, name);
    } else {
        delete rtn;
    }
}

PmatchTransducer * PmatchContainer::get_rtn(const std::string & name)
{
    if (name == "TOP") {
        return toplevel;
    } else {
        return alphabet.get_rtn(name);
    }
}

PmatchContainer::PmatchContainer(void)
{
    // Not used, but apparently needed by swig to construct these
}

bool PmatchAlphabet::is_end_tag(const std::string & symbol)
{
    return symbol.find("@PMATCH_ENDTAG_") == 0 &&
        symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_end_tag(const SymbolNumber symbol) const
{
    return end_tag_map.count(symbol) == 1;
}

bool PmatchAlphabet::is_capture_tag(const std::string & symbol)
{
    return symbol.find("@PMATCH_CAPTURE_") == 0 &&
        symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_capture_tag(const SymbolNumber symbol) const
{
    return capture_tag_map.count(symbol) == 1;
}

bool PmatchAlphabet::is_captured_tag(const std::string & symbol)
{
    return symbol.find("@PMATCH_CAPTURED_") == 0 &&
        symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_captured_tag(const SymbolNumber symbol) const
{
    return captured_tag_map.count(symbol) == 1;
}

bool PmatchAlphabet::is_insertion(const std::string & symbol)
{
    return symbol.find("@I.") == 0 && symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_guard(const std::string & symbol)
{
    return symbol.find("@PMATCH_GUARD_") == 0 && symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_counter(const std::string & symbol)
{
    return symbol.find("@PMATCH_COUNTER_") == 0 && symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_list(const std::string & symbol)
{
    return (symbol.find("@L.") == 0 || symbol.find("@X.") == 0) && symbol.rfind("@") == symbol.size() - 1;
}

bool PmatchAlphabet::is_special(const std::string & symbol)
{
    if (symbol.size() < 3) {
        return false;
    }
    if (is_insertion(symbol) || symbol == "@BOUNDARY@") {
//        || symbol == "@_UNKNOWN_SYMBOL_@" || symbol == "@_IDENTITY_SYMBOL_@"
        return true;
    } else {
        return symbol.find("@PMATCH") == 0 && symbol.at(symbol.size() - 1) == '@';
    }
}

bool PmatchAlphabet::is_printable(const std::string & symbol)
{
    if (symbol.size() < 3) {
        return true;
    }
    return symbol.find("@") != 0 || symbol.at(symbol.size() - 1) != '@';
}

bool PmatchAlphabet::is_guard(const SymbolNumber symbol) const
{
    for(SymbolNumberVector::const_iterator it = guards.begin();
        it != guards.end(); ++it) {
        if(symbol == *it) {
            return true;
        }
    }
    return false;
}

bool PmatchAlphabet::is_counter(const SymbolNumber symbol) const
{
    return (symbol < counters.size() && counters[symbol] != NO_COUNTER);
}

bool PmatchAlphabet::is_input_mark(const SymbolNumber symbol) const
{
    return get_special(Pmatch_input_mark) == symbol;
}

std::string PmatchAlphabet::name_from_insertion(const std::string & symbol)
{
    return symbol.substr(sizeof("@I.") - 1, symbol.size() - (sizeof("@I.@") - 1));
}

std::string PmatchAlphabet::end_tag(const SymbolNumber symbol)
{
    if (end_tag_map.count(symbol) == 0) {
        return "";
    } else {
        return "</" + end_tag_map[symbol] + ">";
    }
}

std::string PmatchAlphabet::start_tag(const SymbolNumber symbol)
{
    if (end_tag_map.count(symbol) == 0) {
        return "";
    } else {
        return "<" + end_tag_map[symbol] + ">";
    }
    
}

PmatchContainer::~PmatchContainer(void)
{
    delete encoder;
    delete toplevel;
}

PmatchAlphabet::~PmatchAlphabet(void)
{
    for (RtnVector::iterator it = rtns.begin();
         it != rtns.end(); ++it) {
        delete *it;
        *it = NULL;
    }

}

std::map<std::string, std::string> PmatchContainer::parse_hfst3_header(std::istream & f)
{
    std::map<std::string, std::string> properties;
    const char* header1 = "HFST";
    unsigned int header_loc = 0; // how much of the header has been found
    int c;
    for(header_loc = 0; header_loc < strlen(header1) + 1; header_loc++)
    {
        c = f.get();
        if(c != header1[header_loc]) {
            break;
        }
    }
    if(header_loc == strlen(header1) + 1)
    {
        unsigned short remaining_header_len;
        f.read((char*) &remaining_header_len, sizeof(remaining_header_len));
        if (f.get() != '\0') {
            HFST_THROW(TransducerHeaderException);
        }
        char * headervalue = new char[remaining_header_len];
        f.read(headervalue, remaining_header_len);
        if (headervalue[remaining_header_len - 1] != '\0') {
            HFST_THROW(TransducerHeaderException);
        }
        int i = 0;
        while (i < remaining_header_len) {
            int length = hfst::size_t_to_int(strlen(headervalue + i));
            std::string property(headervalue + i, headervalue + i + length);
            i += length + 1;
            length = hfst::size_t_to_int(strlen(headervalue + i));
            std::string value(headervalue + i, headervalue + i + length);
            properties[property] = value;
            i += length + 1;
        }
        delete[] headervalue;
        return properties;
    } else // nope. put back what we've taken
    {
        f.unget(); // first the non-matching character
        for(int i = header_loc - 1; i>=0; i--) {
            // then the characters that did match (if any)
            f.unget();
        }
        HFST_THROW(TransducerHeaderException);
    }
}

void PmatchContainer::push_rtn_call(unsigned int return_index, std::string caller)
{
    RtnStackFrame new_top;
    new_top.caller = caller;
    new_top.caller_index = return_index;
    rtn_stack.push(new_top);
}

RtnStackFrame PmatchContainer::rtn_stack_top(void)
{
    return rtn_stack.top();
}

void PmatchContainer::rtn_stack_pop(void)
{
    rtn_stack.pop();
}

void PmatchAlphabet::add_rtn(PmatchTransducer * rtn, std::string const & name)
{
    SymbolNumber symbol = rtn_names[name];
    rtns[symbol] = rtn;
}

bool PmatchAlphabet::has_rtn(std::string const & name) const
{
    if (name == "TOP") {
        return true;
    }
#ifdef NO_CPLUSPLUS_11
    hfst_ol::RtnNameMap::const_iterator it = rtn_names.find(name);
    if (it != rtn_names.end())
    {
        return it->second < rtns.size() && rtns[it->second] != NULL;
    } else {
        return false;
    }
#else	
    return rtn_names.count(name) != 0 &&
        rtn_names.at(name) < rtns.size() && rtns[rtn_names.at(name)] != NULL;
#endif
}

bool PmatchAlphabet::has_rtn(SymbolNumber symbol) const
{
    return symbol < rtns.size() && rtns[symbol] != NULL;
}

PmatchTransducer * PmatchAlphabet::get_rtn(SymbolNumber symbol)
{
    return rtns[symbol];
}

PmatchTransducer * PmatchAlphabet::get_rtn(std::string name)
{
    return rtns[rtn_names[name]];
}

std::string PmatchAlphabet::get_counter_name(SymbolNumber symbol)
{
    if (symbol_table.size() <= symbol) {
        return "INVALID_COUNTER";
    }
    std::string name = symbol_table[symbol];
    if (!is_counter(name)) {
        return "INVALID_COUNTER";
    }
    return name.substr(strlen("@PMATCH_COUNTER_"),
                       name.size() - strlen("@PMATCH_COUNTER_") - 1);
}

SymbolNumber PmatchAlphabet::get_special(SpecialSymbol special) const
{
    return special_symbols.at(special);
}

void PmatchContainer::process(const std::string & input_str)
{
    initialize_input(input_str.c_str());
    unsigned int input_pos = 0;
    unsigned int printable_input_pos = 0;
    running_weight = 0.0;
    stack_depth = 0;
    best_input_pos = 0;

    ++line_number;
    result.clear();
    locations.clear();
    DoubleTape nonmatching_locations;
    while (has_queued_input(input_pos)) {
        best_result.clear();
        SymbolNumber current_input = input[input_pos];
        if (not_possible_first_symbol(current_input)) {
            copy_to_result(current_input, current_input);
            ++input_pos;
            if (locate_mode && alphabet.is_printable(current_input)) {
                ++printable_input_pos;
                nonmatching_locations.push_back(
                    SymbolPair(current_input, current_input));
            }
            continue;
        }
        tape.clear();
        tape_locations.clear();
        unsigned int tape_pos = 0;
        unsigned int old_input_pos = input_pos;
        toplevel->match(input_pos, tape_pos);
        if (candidate_found()) {
            // We got some output
            if (locate_mode) {
                // First we put into the locations vector all the nonmatching parts we've seen
                if (!nonmatching_locations.empty()) {
                    LocationVector ls;
                    Location nonmatching = alphabet.locatefy(printable_input_pos - hfst::size_t_to_uint(nonmatching_locations.size()),
                                                             WeightedDoubleTape(nonmatching_locations, 0.0));
                    nonmatching.output = "@_NONMATCHING_@";
                    ls.push_back(nonmatching);
                    locations.push_back(ls);
                    nonmatching_locations.clear();
                }
                LocationVector ls;
                for (WeightedDoubleTapeVector::iterator it = tape_locations.begin();
                     it != tape_locations.end(); ++it) {
                    ls.push_back(alphabet.locatefy(printable_input_pos,
                                                   *it));
                }
                sort(ls.begin(), ls.end());
                locations.push_back(ls);
                printable_input_pos += (best_input_pos - old_input_pos);
            } else {
                copy_to_result(best_result);
            }
            input_pos = best_input_pos;
        }
        if (!candidate_found() || input_pos == old_input_pos) {
            // If no input was consumed, we move one position up
            copy_to_result(current_input, current_input);
            ++input_pos;
            if (locate_mode && alphabet.is_printable(current_input)) {
                ++printable_input_pos;
                nonmatching_locations.push_back(SymbolPair(current_input, current_input));
            }
        }
    }
    if (locate_mode && !nonmatching_locations.empty()) {
        LocationVector ls;
        Location nonmatching = alphabet.locatefy(printable_input_pos - hfst::size_t_to_uint(nonmatching_locations.size()),
                                                 WeightedDoubleTape(nonmatching_locations, 0.0));
        nonmatching.output = "@_NONMATCHING_@";
        ls.push_back(nonmatching);
        locations.push_back(ls);
    }
}

std::string PmatchContainer::match(const std::string & input,
                                   double time_cutoff)
{
    max_time = time_cutoff;
    if (max_time > 0.0) {
        start_clock = clock();
        call_counter = 0;
        limit_reached = false;
    }
    locate_mode = false;
    process(input);
    return alphabet.stringify(result);
}

LocationVectorVector PmatchContainer::locate(const std::string & input,
                                             double time_cutoff)
{
    max_time = time_cutoff;
    if (max_time > 0.0) {
        start_clock = clock();
        call_counter = 0;
        limit_reached = false;
    }
    locate_mode = true;
    process(input);
    return locations;
}

// A utility comparing function for get_profiling_info
bool counter_comp(std::pair<std::string, unsigned long> l,
                  std::pair<std::string, unsigned long> r)
{
    // Descending order
    return l.second > r.second;
}

std::string PmatchContainer::get_profiling_info(void)
{
    std::stringstream retval;
    size_t max_name_len = 0;
    retval << "Profiling information:\n";
    retval << "  Traversals of Counter() positions:\n";
    std::vector<std::pair<std::string, unsigned long> > counter_name_val_pairs;
    for(SymbolNumber i = 0; i < alphabet.counters.size(); ++i) {
        if (alphabet.counters[i] != NO_COUNTER) {
            std::string counter_name = alphabet.get_counter_name(i);
            if (counter_name.size() > max_name_len) {
                max_name_len = counter_name.size();
            }
            counter_name_val_pairs.push_back(
                std::pair<std::string, unsigned long>(counter_name,
                                                      alphabet.counters[i]));
        }
    }
    std::sort(counter_name_val_pairs.begin(), counter_name_val_pairs.end(),
              counter_comp);
    for(std::vector<std::pair<std::string, unsigned long> >::const_iterator it =
            counter_name_val_pairs.begin(); it != counter_name_val_pairs.end(); ++it) {
        retval << "    " << it->first;
        size_t spacing_counter = max_name_len + 8 - it->first.size();
        while (spacing_counter) {
            retval << " ";
            --spacing_counter;
        }
        retval << it->second << "\n";
    }
    return retval.str();
}

std::string PmatchContainer::get_pattern_count_info(void)
{
    size_t total = 0;
    std::string retval = "Pattern\t\t# of matches\n------------------------\n";
    for (std::map<std::string, size_t>::iterator it = pattern_counts.begin();
         it != pattern_counts.end(); ++it) {
        retval.append(it->first);
        retval.append("\t\t");
        std::ostringstream converter;
        converter << it->second;
        retval.append(converter.str());
        retval.append("\n");
        total += it->second;
    }
    retval.append("------------------------\n");
    std::ostringstream converter;
    converter << total;
    retval.append("Total:\t\t");
    retval.append(converter.str());
    retval.append("\n");
    return retval;
}

void PmatchContainer::copy_to_result(const DoubleTape & best_result)
{
    for (DoubleTape::const_iterator it = best_result.begin();
         it != best_result.end(); ++it) {
        result.push_back(*it);
    }
}

void PmatchContainer::copy_to_result(SymbolNumber input_sym, SymbolNumber output_sym)
{
    result.push_back(SymbolPair(input_sym, output_sym));
}

std::string PmatchAlphabet::stringify(const DoubleTape & str)
{
    std::string retval;
    std::stack<unsigned int> start_tag_pos;
    bool input_contained_printable_symbol = false;
    for (DoubleTape::const_iterator it = str.begin();
         it != str.end(); ++it) {
        if (!input_contained_printable_symbol && is_printable(it->input)) {
            input_contained_printable_symbol = true;
        }
        SymbolNumber output = it->output;
        if (output == special_symbols[entry]) {
            start_tag_pos.push(hfst::size_t_to_uint(retval.size()));
        } else if (output == special_symbols[exit]) {
            if (start_tag_pos.size() != 0) {
                start_tag_pos.pop();
            }
        } else if (is_end_tag(output)) {
            if (container->count_patterns && input_contained_printable_symbol) {
                if ((container->pattern_counts).count(start_tag(output)) == 0) {
                    (container->pattern_counts)[start_tag(output)] = 1;
                } else {
                    (container->pattern_counts)[start_tag(output)] += 1;
                }
            }
            unsigned int pos;
            if (start_tag_pos.size() == 0) {
                std::cerr << "Warning: end tag without start tag\n";
                pos = 0;
            } else {
                pos = start_tag_pos.top();
            }
            if (container->delete_patterns) {
                size_t how_much_to_delete = retval.size() - pos;
                retval.replace(pos, how_much_to_delete, start_tag(output));
            } else if (container->mark_patterns && input_contained_printable_symbol) {
                retval.insert(pos, start_tag(output));
                retval.append(end_tag(output));
            }
        } else {
            if ((!(container->extract_patterns) || start_tag_pos.size() != 0)
                && is_printable(output)) {
                retval.append(string_from_symbol(output));
            }
        }
    }
    return retval;
}

Location PmatchAlphabet::locatefy(unsigned int input_offset,
                                  const WeightedDoubleTape & str)
{
    Location retval;
    retval.start = input_offset;
    retval.weight = str.weight;
    size_t input_mark = 0;
    size_t output_mark = 0;

    // We rebuild the original input without special
    // symbols but with IDENTITIES etc. replaced
    for (DoubleTape::const_iterator it = str.begin();
         it != str.end(); ++it) {
        SymbolNumber input = it->input;
        SymbolNumber output = it->output;
        if (is_end_tag(output)) {
            if (container->count_patterns) {
                if ((container->pattern_counts).count(start_tag(output)) == 0) {
                    (container->pattern_counts)[start_tag(output)] = 1;
                } else {
                    (container->pattern_counts)[start_tag(output)] += 1;
                }
            }
            retval.tag = start_tag(output);
            continue;
        }
        if (is_printable(output)) {
            std::string s = string_from_symbol(output);
            retval.output.append(s);
            retval.output_symbol_strings.push_back(s);
        }
        if (is_printable(input)) {
            std::string s = string_from_symbol(input);
            retval.input.append(s);
            retval.input_symbol_strings.push_back(s);
            ++input_offset;
        }
        if (is_input_mark(output)) {
            retval.output_parts.push_back(output_mark);
            retval.input_parts.push_back(input_mark);
            output_mark = retval.output_symbol_strings.size();
            input_mark = retval.input_symbol_strings.size();
        }
    }
    if (output_mark > 0) {
        retval.output_parts.push_back(output_mark);
    }
    if (input_mark > 0) {
        retval.input_parts.push_back(input_mark);
    }
    retval.length = input_offset - retval.start;
    return retval;
}

bool PmatchContainer::has_unsatisfied_rtns(void) const
{
    return false;
}

std::string PmatchContainer::get_unsatisfied_rtn_name(void) const
{
    return "";
}

bool PmatchContainer::has_queued_input(unsigned int input_pos)
{
    // we catch underflow due to left context checking here
    return input_pos < input.size() && (input_pos + 1 != 0);
}

bool PmatchContainer::vector_matches_input(unsigned int pos, SymbolNumberVector & vec)
{
    if (pos + vec.size() > input.size()) {
        return false;
    }
    for (size_t i = 0; i < vec.size(); ++i) {
        if (input[pos + i] != vec[i]) {
            return false;
        }
    }
    return true;
}

PmatchTransducer::PmatchTransducer(std::istream & is,
                                   TransitionTableIndex index_table_size,
                                   TransitionTableIndex transition_table_size,
                                   PmatchAlphabet & alpha,
                                   std::string _name,
                                   PmatchContainer * cont):
    alphabet(alpha),
    name(_name),
    container(cont)
{
    orig_symbol_count = hfst::size_t_to_uint(alphabet.get_symbol_table().size());
    // initialize the stack for local variables
    LocalVariables local_variables;
    local_variables.flag_state = alphabet.get_fd_table();
    local_variables.tape_step = 1;
    local_variables.max_context_length_remaining = 254;
    local_variables.context = none;
    local_variables.context_placeholder = 0;
    local_variables.default_symbol_trap = false;
    local_variables.negative_context_success = false;
    local_variables.pending_passthrough = false;
    local_stack.push(local_variables);

    // Allocate and read tables
    char * indextab = (char*) malloc(TransitionWIndex::size * index_table_size);
    char * transitiontab = (char*) malloc(TransitionW::size * transition_table_size);
    is.read(indextab, TransitionWIndex::size * index_table_size);
    is.read(transitiontab, TransitionW::size * transition_table_size);
    char * orig_p = indextab;
    index_table.reserve(index_table_size);
    while(index_table_size) {
        index_table.push_back(TransitionWIndex(indextab));
        --index_table_size;
        indextab += TransitionWIndex::size;
    }
    free(orig_p);
    orig_p = transitiontab;
    transition_table.reserve(transition_table_size);
    while(transition_table_size) {
        transition_table.push_back(TransitionW(transitiontab));
        --transition_table_size;
        transitiontab += TransitionW::size;
    }
    free(orig_p);
}

PmatchTransducer::PmatchTransducer(std::vector<TransitionW> transition_vector,
                                   std::vector<TransitionWIndex> index_vector,
                                   PmatchAlphabet & alpha,
                                   std::string _name,
                                   PmatchContainer * cont):
    transition_table(transition_vector),
    index_table(index_vector),
    alphabet(alpha),
    name(_name),
    container(cont)
{
    orig_symbol_count = hfst::size_t_to_uint(alphabet.get_symbol_table().size());
    // initialize the stack for local variables
    LocalVariables local_variables;
    local_variables.flag_state = alphabet.get_fd_table();
    local_variables.tape_step = 1;
    local_variables.max_context_length_remaining = 254;
    local_variables.context = none;
    local_variables.context_placeholder = 0;
    local_variables.default_symbol_trap = false;
    local_variables.negative_context_success = false;
    local_variables.pending_passthrough = false;
    local_stack.push(local_variables);
}

// Precompute which symbols may be at the start of a match.
// For now we ignore default arcs, as does the rest of pmatch.
void PmatchTransducer::collect_possible_first_symbols(void)
{
    SymbolNumberVector input_symbols;
    SymbolNumberVector special_symbol_v = alphabet.get_specials();
    std::set<SymbolNumber> special_symbols(special_symbol_v.begin(),
                                           special_symbol_v.end());
    SymbolTable table = alphabet.get_symbol_table();
    SymbolNumber symbol_count = hfst::size_t_to_uint(table.size());
    for (SymbolNumber i = 1; i < symbol_count; ++i) {
        if (!alphabet.is_like_epsilon(i) &&
            !alphabet.is_end_tag(i) &&
            special_symbols.count(i) == 0 &&
            i != alphabet.get_unknown_symbol() &&
            i != alphabet.get_identity_symbol() &&
            i != alphabet.get_default_symbol())
        {
            input_symbols.push_back(i);
        }
    }
    // always include unknown and identity (once) but not default
    if (alphabet.get_unknown_symbol() != NO_SYMBOL_NUMBER) {
        input_symbols.push_back(alphabet.get_unknown_symbol());
    }
    if (alphabet.get_identity_symbol() != NO_SYMBOL_NUMBER) {
        input_symbols.push_back(alphabet.get_identity_symbol());
    }
    std::set<TransitionTableIndex> seen_indices;
    try {
        collect_first(0, input_symbols, seen_indices);
    } catch (bool e) {
        // If the end state can be reached without any input
        // or we have initial wildcards
        if (e == true) {
            possible_first_symbols.clear();
        }
    }

}

void PmatchTransducer::collect_first_epsilon(TransitionTableIndex i,
                                             SymbolNumberVector const& input_symbols,
                                             std::set<TransitionTableIndex> & seen_indices)
{
    while(true) {
        SymbolNumber output = transition_table[i].get_output_symbol();
        if (transition_table[i].get_input_symbol() == 0) {
            if (!checking_context()) {
                if (!try_entering_context(output)) {
                    collect_first(transition_table[i].get_target(), input_symbols, seen_indices);
                    ++i;
                } else {
                    // We're going to fake through a context
                    collect_first(transition_table[i].get_target(), input_symbols, seen_indices);
                    ++i;
                }
            } else {
                // We *are* checking context and may be done
                if (try_exiting_context(output)) {
                    collect_first(transition_table[i].get_target(), input_symbols, seen_indices);
                    ++i;
                } else {
                    // Don't touch output when checking context
                    collect_first(transition_table[i].get_target(), input_symbols, seen_indices);
                    ++i;
                }
            }
        } else if (alphabet.is_flag_diacritic(
                       transition_table[i].get_input_symbol())) {
            collect_first(transition_table[i].get_target(), input_symbols, seen_indices);
            ++i;
        } else if (alphabet.has_rtn(transition_table[i].get_input_symbol())) {
            possible_first_symbols.insert(transition_table[i].get_input_symbol());
            // collect the inputs from this later
            ++i;
        } else { // it's not epsilon and it's not a flag or Ins, so nothing to do
            return;
        }
    }

}

void PmatchTransducer::collect_first_epsilon_index(TransitionTableIndex i,
                                                   SymbolNumberVector const& input_symbols,
                                                   std::set<TransitionTableIndex> & seen_indices)
{
    if (index_table[i].get_input_symbol() == 0) {
        collect_first_epsilon(
            index_table[i].get_target() - TRANSITION_TARGET_TABLE_START,
            input_symbols, seen_indices);
    }
}

void PmatchTransducer::collect_first_transition(TransitionTableIndex i,
                                                SymbolNumberVector const& input_symbols,
                                                std::set<TransitionTableIndex> & seen_indices)
{
    for (SymbolNumberVector::const_iterator it = input_symbols.begin();
         it != input_symbols.end(); ++it) {
        if (transition_table[i].get_input_symbol() == *it) {
            if (!checking_context()) {
                // if this is unknown or identity, game over
                if (*it == alphabet.get_identity_symbol() ||
                    *it == alphabet.get_unknown_symbol()) {
                    container->reset_recursion();
                    throw true;
                }
                if (alphabet.list2symbols[*it] != NO_SYMBOL_NUMBER) {
                    // If this is a list, collect everything in the list
                    // if it's an exclusionary list, give up
                    if (std::find(alphabet.exclusionary_lists.begin(),
                                  alphabet.exclusionary_lists.end(),
                                  *it)
                        != alphabet.exclusionary_lists.end()) {
                        container->reset_recursion();
                        throw true;
                    }
                    for (SymbolNumberVector::const_iterator sym_it =
                            alphabet.symbol_list_members[alphabet.list2symbols[*it]].begin();
                        sym_it != alphabet.symbol_list_members[alphabet.list2symbols[*it]].end(); ++sym_it) {
                        possible_first_symbols.insert(*sym_it);
                    }
                } else {
                    possible_first_symbols.insert(*it);
                }
            } else {
                // faking through a context check
                collect_first(transition_table[i].get_target(),
                              input_symbols, seen_indices);
            }
        }
    }
}

void PmatchTransducer::collect_first_index(TransitionTableIndex i,
                                           SymbolNumberVector const& input_symbols,
                                           std::set<TransitionTableIndex> & seen_indices)
{
    for (SymbolNumberVector::const_iterator it = input_symbols.begin();
         it != input_symbols.end(); ++it) {
        if (index_table[i+*it].get_input_symbol() == *it) {
            collect_first_transition(index_table[i+*it].get_target() -
                                     TRANSITION_TARGET_TABLE_START,
                                     input_symbols, seen_indices);
        }
    }
}

void PmatchTransducer::collect_first(TransitionTableIndex i,
                                     SymbolNumberVector const& input_symbols,
                                     std::set<TransitionTableIndex> & seen_indices)
{
    if (!container->try_recurse()) {
        container->reset_recursion();
        throw true;
    }
    if (seen_indices.count(i) == 1) {
        container->unrecurse();
        return;
    } else {
        seen_indices.insert(i);
    }
    if (indexes_transition_table(i))
    {
        i -= TRANSITION_TARGET_TABLE_START;
        
        // If we can get to finality without any input,
        // throw a bool indicating that the full input set is needed
        if (transition_table[i].final()) {
            container->reset_recursion();
            throw true;
        }

        collect_first_epsilon(i+1, input_symbols, seen_indices);
        collect_first_transition(i+1, input_symbols, seen_indices);
        
    } else {
        if (index_table[i].final()) {
            container->reset_recursion();
            throw true;
        }
        collect_first_epsilon_index(i+1, input_symbols, seen_indices);
        collect_first_index(i+1, input_symbols, seen_indices);
    }
}

void PmatchContainer::set_properties(void)
{
    count_patterns = false;
    delete_patterns = false;
    extract_patterns = false;
    locate_mode = false;
    mark_patterns = true;
    max_context_length = 254;
    max_recursion = 5000;
    need_separators = true;
}

void PmatchContainer::set_properties(std::map<std::string, std::string> & properties)
{
    for (std::map<std::string, std::string>::iterator it = properties.begin();
         it != properties.end(); ++it) {
        if (it->first == "count-patterns") {
            if (it->second == "on") {
                count_patterns = true;
            } else if (it->second == "off") {
                count_patterns = false;
            }
        } else if (it->first == "delete-patterns") {
            if (it->second == "on") {
                delete_patterns = true;
            } else if (it->second == "off") {
                delete_patterns = false;
            }
        } else if (it->first == "extract-patterns") {
            if (it->second == "on") {
                extract_patterns = true;
            } else if (it->second == "off") {
                extract_patterns = false;
            }
        } else if (it->first == "locate-patterns") {
            if (it->second == "on") {
                locate_mode = true;
            } else if (it->second == "off") {
                locate_mode = false;
            }
        } else if (it->first == "mark-patterns") {
            if (it->second == "on") {
                mark_patterns = true;
            } else if (it->second == "off") {
                mark_patterns = false;
            }
        } else if (it->first == "max-context-length") {
            std::stringstream converter(it->second);
            converter >> max_context_length;
            if (max_context_length == 0) {
                if (it->second != "0") {
                    max_context_length = 254;
                }
            }
        } else if (it->first == "max-recursion") {
            std::stringstream converter(it->second);
            converter >> max_recursion;
            if (max_recursion == 0) {
                if (it->second != "0") {
                    max_recursion = 5000;
                }
            }
        } else if (it->first == "need-separators") {
            if (it->second == "on") {
                need_separators = true;
            } else if (it->second == "off") {
                need_separators = false;
            }
        }
    }
}

void PmatchContainer::initialize_input(const char * input_s)
{
    input.clear();
    char * input_str = const_cast<char *>(input_s);
    char ** input_str_ptr = &input_str;
    SymbolNumber k = NO_SYMBOL_NUMBER;
    SymbolNumber boundary_sym = alphabet.get_special(boundary);
    char * single_codepoint_scratch;
    char * single_codepoint_scratch_orig = NULL;
    if (single_codepoint_tokenization) {
        single_codepoint_scratch = new char[5];
        single_codepoint_scratch_orig = single_codepoint_scratch;
    }
    if (boundary_sym != NO_SYMBOL_NUMBER) {
        input.push_back(boundary_sym);
    }
    while (**input_str_ptr != 0) {
        char * original_input_loc = *input_str_ptr;
        if (single_codepoint_tokenization) {
            int bytes_to_tokenize = nByte_utf8(**input_str_ptr);
            if (bytes_to_tokenize > 0) {
                single_codepoint_scratch = single_codepoint_scratch_orig;
                memcpy(single_codepoint_scratch, *input_str_ptr, bytes_to_tokenize);
                single_codepoint_scratch[bytes_to_tokenize] = '\0';
                k = encoder->find_key(&single_codepoint_scratch);
                if (k != NO_SYMBOL_NUMBER) {
                    (*input_str_ptr) += bytes_to_tokenize;
                }
            }
        } else {
            k = encoder->find_key(input_str_ptr);
        }
        if (k == NO_SYMBOL_NUMBER) {
            // Regular tokenization failed
            // the encoder moves as far as it can during tokenization,
            // we want to go back to be in position to add one utf-8 char
            *input_str_ptr = original_input_loc;
            int bytes_to_tokenize = nByte_utf8(**input_str_ptr);
            if (bytes_to_tokenize == 0) {
                // if utf-8 tokenization fails too, just grab a byte
                bytes_to_tokenize = 1;
            }
            char new_symbol[5];
            memcpy(new_symbol, *input_str_ptr, bytes_to_tokenize);
            new_symbol[bytes_to_tokenize] = '\0';
            (*input_str_ptr) += bytes_to_tokenize;
            alphabet.add_symbol(new_symbol);
            encoder->read_input_symbol(new_symbol, symbol_count);
            k = symbol_count;
            ++symbol_count;
        }
        input.push_back(k);
    }
    if (boundary_sym != NO_SYMBOL_NUMBER) {
        input.push_back(boundary_sym);
    }
    if (single_codepoint_tokenization) {
        delete single_codepoint_scratch_orig;
    }
    return;
}

void PmatchTransducer::match(unsigned int input_tape_pos,
                             unsigned int tape_pos)
{
    local_stack.top().context = none;
    local_stack.top().tape_step = 1;
    local_stack.top().context_placeholder = 0;
    local_stack.top().default_symbol_trap = false;
    get_analyses(input_tape_pos, tape_pos, 0);
}

void PmatchTransducer::rtn_enter(unsigned int input_tape_pos,
                                 unsigned int tape_pos,
                                 std::string caller,
                                 TransitionTableIndex caller_index)
{
    LocalVariables new_top(local_stack.top());
    TransitionTableIndex entry_index;
    if (caller_index == NO_TABLE_INDEX) {
        // we're returning from an rtn end state
        entry_index = container->rtn_stack_top().caller_index;
    } else {
        entry_index = 0;
    }
    new_top.flag_state = alphabet.get_fd_table();
    new_top.tape_step = 1;
    new_top.context = none;
    new_top.context_placeholder = 0;
    new_top.default_symbol_trap = false;
    local_stack.push(new_top);
    container->push_rtn_call(caller_index, caller);
    get_analyses(input_tape_pos, tape_pos, entry_index);
    local_stack.pop();
    container->rtn_stack_pop();
}
    

void PmatchTransducer::rtn_call(unsigned int input_tape_pos,
                                unsigned int tape_pos,
                                std::string caller,
                                TransitionTableIndex caller_index)
{
    container->increase_stack_depth();
    rtn_enter(input_tape_pos, tape_pos, caller, caller_index);
    container->decrease_stack_depth();
}

void PmatchTransducer::rtn_return(unsigned int input_tape_pos,
                                  unsigned int tape_pos,
                                  std::string caller)
{
    container->decrease_stack_depth();
    rtn_enter(input_tape_pos, tape_pos, caller, NO_TABLE_INDEX);
    container->increase_stack_depth();
}

void PmatchTransducer::handle_final_state(unsigned int input_pos,
                                          unsigned int tape_pos)
{
    if (container->get_stack_depth() > 0) {
        // We're not the toplevel, return to caller
        PmatchTransducer * rtn_target =
            container->get_rtn(container->rtn_stack_top().caller);
        rtn_target->rtn_return(input_pos, tape_pos, name);
    } else if (container->is_in_locate_mode()) {
        container->grab_location(input_pos, tape_pos);
    } else {
        container->note_analysis(input_pos, tape_pos);
    }
}

void PmatchContainer::note_analysis(unsigned int input_pos, unsigned int tape_pos)
{
    if ((input_pos > best_input_pos) ||
        (input_pos == best_input_pos &&
         best_weight > running_weight)) {
        best_result = tape.extract_slice(0, tape_pos);
        best_input_pos = input_pos;
        best_weight = running_weight;
    } else if (verbose &&
               input_pos == best_input_pos &&
               best_weight == running_weight) {
        DoubleTape discarded(tape.extract_slice(0, tape_pos));
        std::cerr << "\n\tline " << line_number << ": conflicting equally weighted matches found, keeping:\n\t"
                  << alphabet.stringify(best_result) << std::endl
                  << "\tdiscarding:\n\t"
                  << alphabet.stringify(discarded) << std::endl << std::endl;
    }
}

void PmatchContainer::grab_location(unsigned int input_pos, unsigned int tape_pos)
{
    if (tape_locations.size() != 0) {
        if (input_pos < best_input_pos) {
            // We already have better matches
            return;
        } else if (input_pos > best_input_pos) {
            // The old locations are worse
            tape_locations.clear();
        }
    }
    best_input_pos = input_pos;
    WeightedDoubleTape rv(tape.extract_slice(0, tape_pos), running_weight);
    tape_locations.push_back(rv);
}

SymbolNumberVector PmatchContainer::get_longest_matching_capture(
    SymbolNumber key, unsigned int input_pos)
{
    SymbolNumberVector longest_so_far;
    for (std::vector<std::pair<unsigned int, unsigned int> >::iterator it =
             captures.begin(); it != captures.end(); ++it) {
        SymbolNumberVector slice(input.begin() + it->first, input.begin() + it->second);
        if (vector_matches_input(input_pos, slice)) {
            if (slice.size() <= longest_so_far.size()) {
                continue;
            } else {
                longest_so_far = slice;
            }
        }
    }
    return longest_so_far;
}

void PmatchTransducer::take_epsilons(unsigned int input_pos,
                                     unsigned int tape_pos,
                                     TransitionTableIndex i)
{
    i = make_transition_table_index(i, 0);
    while (is_good(i)) {
        SymbolNumber input = transition_table[i].get_input_symbol();
        SymbolNumber output = transition_table[i].get_output_symbol();
        TransitionTableIndex target = transition_table[i].get_target();
        Weight old_weight = container->get_weight();
        container->increment_weight(transition_table[i].get_weight());
        // We also handle paths where we're checking contexts here
        if (input == 0) {
            if (container->profile_mode) {
                alphabet.count(output);
            }
            if (!checking_context()) {
                if (!try_entering_context(output)) {
                    // no context to enter, regular input epsilon
                    container->tape.write(tape_pos, 0, output);
                    
                    // if it's an entry or exit arc, adjust entry stack
                    if (output == alphabet.get_special(entry)) {
                        container->entry_stack.push(input_pos);
                    } else if (output == alphabet.get_special(exit)) {
                        container->entry_stack.pop();
                    } else if (alphabet.is_capture_tag(output)) {
                        // if it's a capture tag, do the capture
                        container->captures.push_back(
                            std::pair<unsigned int, unsigned int>(container->entry_stack.back(), input_pos));
                    } else if (alphabet.is_captured_tag(output)) {
                        // if it's a captured tag, try each previously
                        // captured sequence
                        SymbolNumberVector cap = container->get_longest_matching_capture(output, input_pos);
                        if (cap.size() != 0) {
                            container->tape.write(tape_pos, cap);
                            get_analyses(input_pos + cap.size(), tape_pos + cap.size(), target);
                        }
                        ++i;
                        container->set_weight(old_weight);
                        continue;
                    }
                    
                    get_analyses(input_pos, tape_pos + 1, target);
                    
                    if (output == alphabet.get_special(entry)) {
                        container->entry_stack.pop_back();
                    } else if (output == alphabet.get_special(exit)) {
                        container->entry_stack.unpop();
                    } else if (alphabet.is_capture_tag(output)) {
                        container->captures.pop_back();
                    }
                } else {
                    check_context(input_pos, tape_pos, i);
                    exit_context();
                }
            } else {
                // We *are* checking context and may be done
                if (try_exiting_context(output)) {
                    // We've successfully completed a context check
                    get_analyses(local_stack.top().context_placeholder, tape_pos, target);
                } else {
                    if (local_stack.top().negative_context_success == true) {
                        // We've succeeded in a negative context, just back out
                        return;
                    } else {
                        // Don't alter tapes when checking context
                        get_analyses(input_pos, tape_pos, target);
                    }
                }
            }
        } else if (alphabet.is_flag_diacritic(input)) {
            take_flag(input, input_pos, tape_pos, i);
        } else if (alphabet.has_rtn(input)) {
            alphabet.get_rtn(input)->rtn_call(input_pos, tape_pos, name, target);
        } else { // it's not epsilon and it's not a flag or Ins, so nothing to do
            container->set_weight(old_weight);
            return;
        }
        ++i;
        container->set_weight(old_weight);
    }
}

void PmatchTransducer::check_context(unsigned int input_pos,
                                     unsigned int tape_pos,
                                     TransitionTableIndex i)
{
    // The context placeholder remembers the position in the input before
    // a context check. If the context check is successful, the placeholder
    // will be used as the input position going forwards.
    local_stack.top().context_placeholder = input_pos;
    if (local_stack.top().context == LC ||
        local_stack.top().context == NLC) {
        // Jump to the left-hand side of the input
        input_pos = container->entry_stack.top() - 1;
    }
    get_analyses(input_pos, tape_pos, transition_table[i].get_target());

    // In case we have a negative context, we check to see if the context matched.
    // If it didn't, we schedule a passthrough arc after we've processed epsilons.
    // We also manually reset the context information.
    if(local_stack.top().context == NLC || local_stack.top().context == NRC) {
        local_stack.top().context = none;
        local_stack.top().tape_step = 1;
        if (local_stack.top().negative_context_success == false) {
            exit_context();
            local_stack.top().pending_passthrough = true;
        }
    }
}

void PmatchTransducer::take_flag(SymbolNumber input,
                                 unsigned int input_pos,
                                 unsigned int tape_pos,
                                 TransitionTableIndex i)
{
    std::vector<short> old_values(local_stack.top().flag_state.get_values());
    if (local_stack.top().flag_state.apply_operation(
            *(alphabet.get_operation(input)))) {
        // flag diacritic allowed
        // generally we shouldn't care to write flags
//                container->tape.write(tape_pos, input, output);
        get_analyses(input_pos, tape_pos, transition_table[i].get_target());
    }
    local_stack.top().flag_state.assign_values(old_values);
}

void PmatchTransducer::take_transitions(SymbolNumber input,
                                        unsigned int input_pos,
                                        unsigned int tape_pos,
                                        TransitionTableIndex i)
{
    i = make_transition_table_index(i, input);
    
    while (is_good(i)) {
        SymbolNumber this_input = transition_table[i].get_input_symbol();
        SymbolNumber this_output = transition_table[i].get_output_symbol();
        TransitionTableIndex target = transition_table[i].get_target();
        if (this_input == NO_SYMBOL_NUMBER) {
            return;
        } else if (this_input == input) {
            Weight old_weight = container->get_weight();
            container->increment_weight(transition_table[i].get_weight());
            if (!checking_context()) {
                if (this_output == alphabet.get_identity_symbol() ||
                    (this_output == alphabet.get_unknown_symbol()) ||
                    (alphabet.list2symbols[this_output] != NO_SYMBOL_NUMBER)) {
                // we got here via a meta-arc, so look back in the
                // input tape to find the symbol we want to write
                    this_output = container->input[input_pos];
                }
                if (this_input == alphabet.get_identity_symbol() ||
                    (this_input == alphabet.get_unknown_symbol()) ||
                    (alphabet.list2symbols[this_input] != NO_SYMBOL_NUMBER)) {
                    this_input = container->input[input_pos];
                }
                if (this_input == alphabet.get_special(Pmatch_passthrough)) {
                    get_analyses(input_pos, tape_pos, target); // awkward
                } else {
                    container->tape.write(tape_pos, this_input, this_output);
                    get_analyses(input_pos + 1, tape_pos + 1, target);
                }
            } else {
                // Checking context so don't touch output
                if (local_stack.top().max_context_length_remaining > 0) {
                    local_stack.top().max_context_length_remaining -= 1;
                    get_analyses(input_pos + local_stack.top().tape_step, tape_pos, target);
                    local_stack.top().max_context_length_remaining += 1;
                }
            }
            local_stack.top().default_symbol_trap = false;
            container->set_weight(old_weight);
        } else {
            return;
        }
        ++i;
    }
}

void PmatchTransducer::get_analyses(unsigned int input_pos,
                                    unsigned int tape_pos,
                                    TransitionTableIndex i)
{
    if (container->max_time > 0.0) {
        ++container->call_counter;
        // Have we spent too much time?
        if (container->limit_reached ||
            (container->call_counter % 1000000 == 0 &&
             (container->candidate_found() &&
              // if we have at least something, stop doing more work
              (((double)(clock() - container->start_clock)) / CLOCKS_PER_SEC) > container->max_time))) {
            container->limit_reached = true;
            return;
        }
    }
    if (!container->try_recurse()) {
        if (container->verbose) {
            std::cerr << "pmatch: out of stack space, truncating result\n";
        }
        return;
    }
    local_stack.top().default_symbol_trap = true;
    take_epsilons(input_pos, tape_pos, i + 1);
    if (local_stack.top().pending_passthrough == true) {
        local_stack.top().pending_passthrough = false;
        // A negative context failed (successfully)
        take_transitions(alphabet.get_special(Pmatch_passthrough),
                         input_pos, tape_pos, i+1);
    }
    // Check for finality even if the input string hasn't ended
    if (is_final(i)) {
        Weight old_weight = container->get_weight();
        container->increment_weight(get_weight(i));
        handle_final_state(input_pos, tape_pos);
        container->set_weight(old_weight);
    }
    
    SymbolNumber input;
    if (!container->has_queued_input(input_pos)) {
        return;
    } else {
        input = container->input[input_pos];
    }
    
    if (alphabet.symbol2lists[input] != NO_SYMBOL_NUMBER) {
// At least one symbol list could allow this symbol
        for(SymbolNumberVector::const_iterator it =
                alphabet.symbol_lists[alphabet.symbol2lists[input]].begin();
            it != alphabet.symbol_lists[alphabet.symbol2lists[input]].end(); ++it) {
            take_transitions(*it, input_pos, tape_pos, i+1);
        }
    }
    // The "normal" case where we have a regular input symbol
    if (input < orig_symbol_count) {
        take_transitions(input, input_pos, tape_pos, i+1);
    } else {
        if (alphabet.get_identity_symbol() != NO_SYMBOL_NUMBER) {
            take_transitions(alphabet.get_identity_symbol(), input_pos, tape_pos, i+1);
        }
        if (alphabet.get_unknown_symbol() != NO_SYMBOL_NUMBER) {
            take_transitions(alphabet.get_unknown_symbol(), input_pos, tape_pos, i+1);
        }
    }
    container->unrecurse();
}

bool PmatchTransducer::checking_context(void) const
{
    return local_stack.top().context != none;
}

bool PmatchTransducer::try_entering_context(SymbolNumber symbol)
{
    if (symbol == alphabet.get_special(LC_entry)) {
        local_stack.top().context = LC;
        local_stack.top().tape_step = -1;
        local_stack.top().max_context_length_remaining =
            container->max_context_length;
        return true;
    } else if (symbol == alphabet.get_special(RC_entry)) {
        local_stack.top().context = RC;
        local_stack.top().tape_step = 1;
        local_stack.top().max_context_length_remaining =
            container->max_context_length;
        return true;
    } else if (symbol == alphabet.get_special(NLC_entry)) {
        local_stack.top().context = NLC;
        local_stack.top().tape_step = -1;
        local_stack.top().max_context_length_remaining =
            container->max_context_length;
        return true;
    } else if (symbol == alphabet.get_special(NRC_entry)) {
        local_stack.top().context = NRC;
        local_stack.top().tape_step = 1;
        local_stack.top().max_context_length_remaining =
            container->max_context_length;
        return true;
    } else {
        return false;
    }
}

bool PmatchTransducer::try_exiting_context(SymbolNumber symbol)
{
    switch (local_stack.top().context) {
    case LC:
        if (symbol == alphabet.get_special(LC_exit)) {
            exit_context();
            return true;
        } else {
            return false;
        }
    case RC:
        if (symbol == alphabet.get_special(RC_exit)) {
            exit_context();
            return true;
        } else {
            return false;
        }
    case NRC:
        if (symbol == alphabet.get_special(NRC_exit)) {
            local_stack.top().negative_context_success = true;
            return false;
        }
    case NLC:
        if (symbol == alphabet.get_special(NLC_exit)) {
            local_stack.top().negative_context_success = true;
            return false;
        }
    default:
        return false;
    }
}

void PmatchTransducer::exit_context(void)
{
    local_stack.top().context = none;
    local_stack.top().negative_context_success = false;
    local_stack.top().tape_step = 1;
}

}

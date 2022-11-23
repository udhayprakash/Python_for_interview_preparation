def arrange(sentence):
    sentence = sentence.rstrip(".").split()
    return " ".join(sorted(sentence, key=lambda wd: len(wd))).capitalize() + "."


if __name__ == "__main__":
    assert (
        arrange("The lines are printed in reverse order.")
        == "In the are lines order printed reverse."
    )
    assert arrange("Here i come.") == "I here come."
    assert arrange("I love to code.") == "I to love code."
    assert (
        arrange("Aibohphobia is a joke term used to describe the fear of palindromes.")
        == "A is to of the joke term used fear describe aibohphobia palindromes."
    )
    assert arrange("The the the the.") == "The the the the."
    assert (
        arrange(
            "Also notice that preprocessor statements which is highlighted appear at the start of the program these statements cause the contents of the header file stdio and ctype to inserted into the program the compilation process begins the information contains in these files is essential for the proper functioning of the library functions getchar putchar and toupper."
        )
        == "Is at of of to in is of the the the the and the the the for the the and also that file into which start these cause stdio ctype these files notice appear header begins proper program program process library getchar putchar toupper contents inserted contains essential functions statements statements highlighted compilation information functioning preprocessor."
    )
    assert arrange("Abcdefghijklomnopqrstuvwxyz.") == "Abcdefghijklomnopqrstuvwxyz."
    assert (
        arrange("A bb ccc ddd eeee fffff gggggg hhhhhhhh iiiiiiiiii.")
        == "A bb ccc ddd eeee fffff gggggg hhhhhhhh iiiiiiiiii."
    )
    assert (
        arrange("Aaaaaaaaaaaaaaaaaaaa bbbbbbbbb ccccccc dddd eee fff gg hh ii jj kk l.")
        == "L gg hh ii jj kk eee fff dddd ccccccc bbbbbbbbb aaaaaaaaaaaaaaaaaaaa."
    )
    assert (
        arrange(
            "Aaaaaaaaaaaaaaaaaaaa gg hh fff dddd ccccccc aaaaaaaaaaaaaaaaaaaa iijjkkeee oo mmmmmmmmmm nnppp."
        )
        == "Gg hh oo fff dddd nnppp ccccccc iijjkkeee mmmmmmmmmm aaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaa."
    )

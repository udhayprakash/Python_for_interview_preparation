#!/usr/bin/python3
"""
Purpose:
"""
import re


def tableOfContents(text):
    section_lines = re.findall("^#+.*", text, re.M)
    result = []
    processed_lines = ""
    for section_line in section_lines:
        if re.search("^#+.*", section_line):
            no_of_hashes = len(re.search("^#+", section_line).group())
            if not result:
                processed_line = "1. " + section_line.lstrip(" #")
            else:
                prev_sec_nums = re.findall("\d+", result[-1][0])
                if result[-1][-1] == no_of_hashes:
                    prev_sec_nums[-1] = str(int(prev_sec_nums[-1]) + 1) + "."
                elif result[-1][-1] < no_of_hashes:
                    prev_sec_nums.append("1.")
                else:  # result[-1][-1] > no_of_hashes:
                    del prev_sec_nums[-1]
                    prev_sec_nums[-1] = str(int(prev_sec_nums[-1]) + 1) + "."

                processed_line = (
                    ".".join(prev_sec_nums) + " " + section_line.lstrip(" #")
                )
            result.append((processed_line, no_of_hashes))
            processed_lines += processed_line + "\n"
    return processed_lines


if __name__ == "__main__":
    print(
        tableOfContents(
            """
    # Cars
    Cars came into global use during the 20th century
    Most definitions of car say they run primarily on roads
    ## Sedan
    Sedan's first recorded use as a name for a car body was in 1912
    ## Coupe
    A coupe is a passenger car with a sloping rear roofline and generally two doors
    ## SUV
    The predecessors to SUVs date back to military and low-volume models from the late 1930s
    There is no commonly agreed definition of an SUV, and usage varies between countries.
    """
        )
    )
    print()

    print(
        tableOfContents(
            """
    10
    # Games
    ## Board
    ## Computer
    ## Zero sum
    ## Multiplayer
    # Strategies
    ## Greedy
    ## Tree pruning
    ## Others
    # Summary
    """
        )
    )
    print()

    print(
        tableOfContents(
            """
    # Alphard escortage diadromous Roselane pronenesses
    # spermagonium acmes soundproof ragtags Goniodoridae
    ## narcotico-irritant warproof hypoactivity nondangerousness
    # hekhsher heterize decomposing enoughs unpolite Podostomata
    # supergroups shat diphthongalize ancestor frictionally
    # nonretardatory enactable osmose tuberculocele immature
    # myelopetal biographers aptly bryonidin phalangerine
    # urosomite timepiece enchequer menotyphlic containable
    # negativity shipwrecking muhly abasias gapping albus
    ## cardioids long-windedness nonbody Endothia thriftshop
    # outlearns disaccustom destigmatization balsamaceous ph{-truncated-}
    """
        )
    )

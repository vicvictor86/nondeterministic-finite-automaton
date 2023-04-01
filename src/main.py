from NonDeterministAutomata import NFA
from NonDeterministAutomata import from_txt
from examples import *

while True:
    option = input("Choose an option: \n1 - Example 1\n2 - Example 2\n3 - Example 3\n4 - Example 4\n5 - Example 5\n6 - Load a new example for txt\n0 - Exit\nYour option: ")
    if option == "0":
        print("Exiting...")
        break
    else:
        example = option
        if example == "1":
            nfae = example1()
        elif example == "2":
            nfae = example2()
        elif example == "3":
            nfae = example3()
        elif example == "4":
            nfae = example4()
        elif example == "5":
            nfae = example5()
        elif example == "6":
            file = input("File name: ")
            try:
                nfae = from_txt(file)
            except Exception as e:
                # print("Error while reading the file")
                print(e)
                continue
        else:
            print("\n-> Invalid option\n")
            continue
        
        option = input("Choose an option: \n1 - Convert NFAE to NFA\n2 - Recognition\nYour option: ")
        if option == "1":
            print(f"NFAE: {nfae}")
            print(f"  Transitions: {nfae.get_transitions()}")
            nfa = nfae.convertNFAEtoNFA()
            print(f"NFA: {nfa}")
            print(f"  Transitions: {nfa.get_transitions()}")
        elif option == "2":
            if example != "4" and example != "5" and example != "6":
                print("This example is not for recognition, please choose another one\n")
            else:
                word = input("Word: ")
                print(f"\nReconhecimento da palavra {word}: {nfae.recognition(word)}\n")
        else:
            print("\n-> Invalid option\n")
            continue
# GeoLogical: Currently a paleontological database, may add more geological topics in near future.
# Timeline sourced from: https://www.nps.gov/subjects/geology/time-scale.htm

print("\n🔬 Welcome to the Geological Database 🌍")

while True:
    print("\nEras:\n🐒 (A) Cenozoic (0.01-66 MYA)\n🦖 (B) Mesozoic (66-251.9 MYA)\n🦈 (C) Paleozoic (251.9-541 MYA)"
          "\n🦠 (D) Proterozoic (541-2500 MYA)\n💧 (E) Archean (2500-4000 MYA)\n🌋 (F) Hadean (4000-4600 MYA)")

    choice = input("\nWhich era would you like to explore? Enter here: ").strip().capitalize()

    eras = {
        "A": "Cenozoic", "B": "Mesozoic", "C": "Paleozoic",
        "D": "Precambrian", "E": "Precambrian", "F": "Precambrian",
        "Cenozoic": "Cenozoic", "Mesozoic": "Mesozoic", "Paleozoic": "Paleozoic",
        "Proterozoic": "Precambrian", "Archean": "Precambrian", "Hadean": "Precambrian"
    }

    era_periods = {
        "Cenozoic": ["Quaternary", "Neogene", "Paleogene"],
        "Mesozoic": ["Cretaceous", "Jurassic", "Triassic"],
        "Paleozoic": ["Permian", "Pennsylvanian", "Mississippian", "Devonian", "Silurian", "Ordovician", "Cambrian"],
        "Precambrian": ["Precambrian"]
    }

    era_facets = {
        "Cenozoic": "Following a mass extinction, early primates appear, large fauna go extinct, and ice ages occur.",
        "Mesozoic": "First dinosaurs and mammals emerge. Ends with the mass extinction of dinosaurs.",
        "Paleozoic": "Explosion of ocean life, first land flora, amphibians, reptiles, and the formation of Pangaea.",
        "Precambrian": "Early life evolves, first multicellular organisms arise, and early supercontinents form."
    }

    period_fauna = {
        "Quaternary": ["Mastodon", "Neanderthal", "Smilodon", "Giant Ground Sloth", "Cave Lion"],
        "Neogene": ["Amphicyon", "Dinotherium", "Dryopithecus", "Terror Bird", "Wooly Rhinoceros"],
        "Paleogene": ["Andrewsarchus", "Basilosaurus", "Brontotherium", "Gastornis", "Hyaenodon"],
        "Cretaceous": ["Mosasaurus", "Velociraptor", "Ankylosaurus", "Tyrannosaurus", "Solenodon"],
        "Jurassic": ["Allosaurus", "Liopleurodon", "Archaeopteryx", "Diplodocus", "Stegosaurus"],
        "Triassic": ["Plateosaurus", "Pterosaurs", "Ichthyosaurs", "Lystrosaurus", "Postosuchus"],
        "Permian": ["Dimetrodon", "Diplocaulus", "Helicoprion", "Biarmosuchia", "Gorgonopsia"],
        "Pennsylvanian": ["Hylonomus", "Meganeura", "Tullimonstrum", "Trilobites", "Ferns"],
        "Mississippian": ["Early Snails", "Lungfishes", "Coelacanth", "First Amphibians", "Crinoids"],
        "Devonian": ["Tiktaalik", "Dunkleosteus", "Acanthostega", "Arthropleura", "First Lobe-Finned Fishes"],
        "Silurian": ["Placoderms", "Sea Scorpions", "Trilobites", "Colonial Corals", "Cystoidea"],
        "Ordovician": ["Endoceratidae", "Nautilidae", "Aegirocassis", "Bryozoa", "Sea Urchins"],
        "Cambrian": ["Anomalocaris", "Wiwaxia", "Hallucigenia", "Vetulicola", "Walking Bivalves"],
        "Precambrian": ["Sponges", "Jellyfish", "Sea Anemones", "Segmented Flatworms", "Cyanobacteria"]
    }

    if choice == "D":
        print("\n🌍 Proterozoic Era:\nSummary: Multicellular life rises through endosymbiosis. Formation of early "
              "supercontinent and first iron deposits.")
        continue  # Skip the rest and restart loop

    if choice == "E":
        print("\n🌍 Archean Era:\nSummary: Oldest known Earth rocks discovered come from this era. Earliest bacteria "
              "and algae.")
        continue  # Skip the rest and restart loop

    if choice == "F":
        print("\n🌍 Hadean Era:\nSummary: Earth's crust is formed through hundreds of millions of years of volcanic "
              "chaos.")
        continue  # Skip the rest and restart loop

    era_name = eras.get(choice)
    if era_name:
        print(f"\n🌍 {era_name} Era's Period(s):")
        for period in era_periods[era_name]:
            print(f"- {period}")
        print("\nThe", era_name, "Era Summary:")
        print(era_facets.get(era_name, "No detailed summary available."))

        fa_choice = input("\nWould you like to see popular fauna of these periods? (Y/N): ").strip().upper()
        if fa_choice == "Y":
            p_choice = input("Which period fauna would you like to see? ").strip().title()
            if p_choice in period_fauna:
                print(f"\n🐾 {p_choice} Period's Fauna:")
                for fauna in period_fauna[p_choice]:
                    print(f"- {fauna}")
            else:
                print("❌ Invalid period. Please enter a valid period name from the list above.")
    else:
        print("❌ Invalid choice. Please enter an era from the list.")

    fin_choice = input("\nWould you like to examine another era? (Y/N): ").strip().upper()
    if fin_choice == "N":
        break



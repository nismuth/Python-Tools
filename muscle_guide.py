# Muscle Guide: tells the user different regions' muscles and recommends workouts

print("\nWelcome to the Muscle Guide.")

while True:
    print("\nWhich muscle region would you like to see?\n1) Face\n2) Neck\n3) Shoulders\n4) Chest\n5) Back\n6) Arms"
          "\n7) Thighs\n8) Calves\n9) Glutes\n10) Hamstrings")
    choice = input("Enter here (1-10): ")

    muscle_groups = {  # Muscles dictionary
        "1": ["masseter", "orbucularis oris", "zygomaticus major"],  # Face
        "2": ["trapezius", "sternocleidomastoid"],  # Neck
        "3": ["trapezius", "deltoids anterior + middle heads"],  # Shoulders
        "4": ["pectoralis major + minor"],  # Chest
        "5": ["teres minor", "rhomboid major", "infraspinatus", "teres major", "posterior head"],  # Back
        "6": ["biceps brachii - short + long", "triceps brachii long + lateral heads", "medial head",  # Arms
              "brachioradialis", "pronator teres", "palmaris longus", "extensor carpi ulnaris",
              "flexor carpi radialis", "abductor pollicis longus", "extensor pollicis brevis", "extensor pollicis longus"],
        "7": ["tensor fasciae latae", "sartorius", "pectineus", "adductor longus", "gracilis",  # Thighs
              "rectus femoris", "vastus lateralis", "vastus medialis"],
        "8": ["gastrocnemius", "tibialis anterior", "peroneus longus", "soleus"],  # Calves
        "9": ["gluteus medius", "gluteus maximus"],  # Glutes
        "10": ["biceps femoris", "semitendinosus", "semimembranosus"]  # Hamstrings
    }

    workouts = {  # Exercises dictionary
        "1": ["Cheek Lifts", "Jawline Resistance", "Lip Pull"],  # Face
        "2": ["Neck Tilts", "Neck Resistance Exercise", "Chin Tucks"],  # Neck
        "3": ["Overhead Shoulder Press", "Lateral Raises", "Face Pulls"],  # Shoulders
        "4": ["Push-Ups", "Bench Press", "Chest Flys"],  # Chest
        "5": ["Pull-Ups", "Bent-Over Rows", "Deadlifts"],  # Back
        "6": ["Bicep Curls", "Triceps Dips", "Forearm Wrist Curls"],  # Arms
        "7": ["Squats", "Lunges", "Leg Press"],  # Thighs
        "8": ["Standing Calf Raises", "Seated Calf Raises", "Jump Rope"],  # Calves
        "9": ["Hip Thrusts", "Bulgarian Split Squats", "Step-Ups"],  # Glutes
        "10": ["Romanian Deadlifts", "Nordic Curls", "Lying Hamstring Curls"]  # Hamstrings
    }

    if choice in muscle_groups:  # If input is in the muscles dictionary - prints corresponding muscles
        print("\nMuscles in this region:")
        for muscle in muscle_groups[choice]:
            print(f"- {muscle}")
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

    ex_choice = input("\nWould you like to see exercises for this area? (Y/N): ").upper()

    if ex_choice == "Y":  # If yes to exercises - prints workouts corresponding to muscle region
        print("\nWorkouts for this muscle group:")
        for workout in workouts[choice]:
            print(f"- {workout}")
    else:
        print("Invalid choice. Please enter Y or N.")

    fin_choice = input("\nWould you like to assess another region? (Y/N): ").upper()  # Restart or end program
    if fin_choice == "Y":
        continue
    if fin_choice == "N":
        break

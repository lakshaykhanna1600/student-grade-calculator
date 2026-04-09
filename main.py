def main():
    subject_count = int(input("How many subjects do you have? "))
    scores = []

    # collect each subject's name and score from the user
    for i in range(subject_count):
        entry = input(f"Enter subject {i + 1} name and score separated by a colon (e.g. Math:98): ")
        subject_name, raw_score = entry.split(":")
        raw_score = int(raw_score)
        scores.append(raw_score)
        get_grade(subject_name, raw_score)

    display_overall(subject_count, scores)


        # prints the grade for a single subject based on the score
def get_grade(subject, score):
    if score < 0 or score > 100:
        print(f"  Invalid score entered for {subject}.")
    elif 90 <= score <= 100:
        print(f"  {subject}: Grade A")
    elif 80 <= score < 90:
        print(f"  {subject}: Grade B")
    elif 70 <= score < 80:
        print(f"  {subject}: Grade C")
    elif 60 <= score < 70:
        print(f"  {subject}: Grade D")
    else:
        print(f"  {subject}: Grade F")


        # calculates and displays overall percentage and final grade
def display_overall(subject_count, scores):
    total_obtained = sum(scores)
    total_possible = subject_count * 100
    percentage = (total_obtained / total_possible) * 100

    print(f"\n--- Overall Result ---")
    print(f"Total Marks   : {total_obtained} / {total_possible}")
    print(f"Percentage    : {percentage:.2f}%")

    if percentage < 0 or percentage > 100:
        print("Invalid data entered.")
    elif 90 <= percentage <= 100:
        print("Overall Grade : A")
    elif 80 <= percentage < 90:
        print("Overall Grade : B")
    elif 70 <= percentage < 80:
        print("Overall Grade : C")
    elif 60 <= percentage < 70:
        print("Overall Grade : D")
    else:
        print("Overall Grade : F")


main()
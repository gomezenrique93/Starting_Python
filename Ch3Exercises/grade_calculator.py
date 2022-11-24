#Prompt user to enter scores for test 1 and test 2
test_one_score = int(input("Enter score for Test 1: "))
if test_one_score < 0 or test_one_score > 25:
    print("Please enter a score between 0 and 25") 
test_two_score = int(input("Enter score for Test 2: "))
if test_two_score < 0 or test_two_score > 25:
    print("Please enter a score between 0 and 25") 
#Prompt user for exam score
exam_score = int(input("Enter score for the main Exam: "))


if test_one_score + test_two_score >= 50 and exam_score >= 25:
    cumulative_score = test_one_score + test_two_score + exam_score
    if cumulative_score >= 80:
        print("Disinction")
    elif cumulative_score < 80 and cumulative_score >= 60:
        print("Credit")
    elif cumulative_score < 60 and cumulative_score >= 59:
        print("Pass")
else:
    print("Fail")




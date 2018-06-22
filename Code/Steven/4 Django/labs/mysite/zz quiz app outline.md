Models:

Quiz: just a set of questions.
Questions: (has ForeignKey Quiz)
Answers (has ForeignKey Question).

Each Question:
1. can have as many answer one likes 
2. but can have one or many correct answers. 
So the correct answer will have its “correct” boolean flag ‘True’.

Each Quiz:
Phase 1.1  1 quiz, fixed length.

2 quizes.  User selects which quiz.  



Phase 1: The quiz is for any user.

Phase 2: The quiz is associated with a specific user.

Phase 3: Score based on percentage of questions answered correctly.  
A high score list is maintained.

Frontend:

    Provide a way to create/edit a Question with answers (Use Inline Form).
    Also a way to create a quiz , and keep on adding questions to it .

That’s it . These are the basics .

ill have as many questions as user wants .
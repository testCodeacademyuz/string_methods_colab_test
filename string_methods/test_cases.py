test_cases = {
    "taskOne":[
        # A variable of type string is given. Find its length.
        {
            "input":["python code"],
            "expected":11
        },
        {
            "input": ["hello world."],
            "expected": 12
        }
    ],
    "taskTwo":[
        # A string type variable is given. Return True if its length is even. Return False if its length is odd.
        {
            "input": ["python3"],
            "expected": False
        },
        {
            "input": ["django"],
            "expected": True
        }
    ],
    "taskThree":[
        # String type variables a and b are given. Return True if the length is equal. If not equal, return False.
        {
            "input": ["python", "django"],
            "expected": True
        },
        {
            "input": ["python", " "],
            "expected": False
        },
        {
            "input": [" ", " "],
            "expected": True
        },
    ],

    "taskFour":[
        # A string variable s is given. Return the "*" sign that is equal to the length of this variable.
        {
            "input": ["python"],
            "expected": "******"
        },
        {
            "input": ["***"],
            "expected": "***"
        },
        {
            "input": ["  "],
            "expected": "**"
        },
    ],

    # Given two strings, s1 and s2. Find their total length.
    "taskFive":[
        {
            "input": ["python", "django"],
            "expected": 12
        },
        {
            "input": ["backend", "frontend"],
            "expected": 15
        },
        {
            "input": ["start", " "],
            "expected": 6
        },
    ],

# Given two strings, s1 and s2. Return the shortest length between them.
    "taskSix":[
        {
            "input": ["codeacademy", "advantage"],
            "expected": "advantage",
        },
        {
            "input": ["academy", "codeacademy"],
            "expected": "academy",
        },
        {
            "input": ["python", "django"],
            "expected": "django"
        }
    ],
    # Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    "taskSeven":[
        {
            "input": ["python", "django", "codeacademy"],
            "expected": "[codeacademy]"
        },
        {
            "input": ["python", "django", "codeacademy", "advantage."],
            "expected": "[codeacademy]"
        },
        {
            "input": ['    ', '  '],
            "expected": "[]"
        },
    ],
    # Given variable type string s. Return the character in the muddle. If the length is even, return two characters in the middle
    "taskEight":[
        {
            "input":["django"],
            "expected": "an"
        },
        {
            "input": ["codeacademy"],
            "expected": "c"
        },
        {
            "input": ["python"],
            "expected": "th"
        },
    ],
    # Given two non-negative integers, num1 and num2 represented as string. Return the sum of num1 and num2 as a string.
    "taskNine":[
        {
            "input": ['0','10'],
            "expected": '10'
        },
        {
            "input": ['11', '10'],
            "expected": "21"
        }
    ],
    # A string of length three is given. Check that it is a palindrome. Return True if the palindrome is False otherwise
    "taskTen":[
        {
            "input": ["man"],
            "expected": False
        },
        {
            "input": ["dad"],
            "expected": True
        },
        {
            "input": ["python"],
            "expected": False
        },
        {
            "input": ["wow"],
            "expected": True
        },
    ]
}

Pre-Interview Questions.

Please keep your answers specific to Python, as answering these questions in any other language or form will be marked as a failure.

    1. Anagram is a word, phrase, or name formed by rearranging the letters of another. For example: Silent is an Anagram of Listen.

Write an example program that determines if a pair of words are Anagrams.

    2. Write a Python function that takes in a list of integers (0 through 10) and returns the sum of all the even numbers in the list.

    3. Write a Python function that takes in a list of integers (in this case use 1, -2, 3, 4, -5 and 6) and returns the maximum sum of any contiguous subarray of the list. A subarray is a contiguous portion of the list.

    4. Network devices are identified by its MAC address, which is 6 byte / 12 hex characters (1234ABCD5678 for example). A RESTful API exists to check the status of a network device (http://localhost:8000/device/check/1234ABCD5678, another example.)

Assume a large dataset exists that contains a large set of device identifiers in the form of MAC addresses (over 10,000+). The RESTful API can take around 5 seconds to complete a single status check, so checking device status is a relatively long running task. Also assume that the device identifiers (MAC addresses) come from a data source / stream that separates each MAC address by a newline.

Write a python solution that processes MAC address with the goal of: minimizing runtime, minimizing resource usage and generalizing methods and procedures.

import java.lang.IllegalArgumentException
import java.util.Random

fun main(args: Array<String>) {
    val CURRENT = false

    if(CURRENT) {
        println("Hello, world!")

        /*****  Basics *****/

        // Immutable (unchangeable) variables.
        val name = "Jerry"
        // Mutable (changeable) variables.
        var favNum = 7

        // Types can be specified.
        var bigInt: Int = Int.MAX_VALUE
        var smallInt: Int = Int.MIN_VALUE

        println("$smallInt - " + bigInt)

        // Types (Long, Double, Float, Boolean, Short, Byte, Char, String) all objects.

        /* Type checking */
        println("Is bigInt an int? ${bigInt is Int}")
        // println("Is name an int? ${name is Int}")

        /* Casting */
        println("double to int: ${3.14.toInt()}")
        println("char to int: ${'A'.toInt()}")
        println("int to char: ${65.toChar()}")

        /* Strings */
        val str = "Some string."
        val longStr = """
            this is a long string.
        """
        var fname: String = "Doug"
        var lname: String = "Smith"
        fname = "Sally"
        var fullName = fname + " " + lname

        println("Name: $fullName")
        var len = fullName.length

        var str1 = "hello"
        var str2 = "Hello"
        println("equal? ${str1.equals(str2)}")
        println("A".compareTo("B"))
        println("2nd index: ${str1.get(2)} ${str1[2]}")
        println("substring: ${str1.subSequence(2, 4)}")
        println("contains: ${str1.contains("ello")}")

        /***** Arrays *****/
        var arr = arrayOf(1, 1.23, "str")
        println(arr[1])
        arr[1] = 3.14

        println(arr.size)
        println(arr.contains("str"))

        var subArr = arr.copyOfRange(0, 1)
        println("First: ${arr.first()}")
        println("str's index: ${arr.indexOf("str")}")

        var squareArr = Array(5, { x -> x * x })
        println(squareArr[2])

        var intArray: Array<Int> = arrayOf(1, 2, 3)

        /* Ranges */
        val oneToTen = 1..10
        val alpha = "A".."Z"
        println("R is in alpha? ${"R" in alpha}")

        val tenToOne = 10.downTo(1)
        val twoToTwenty = 2.rangeTo(20)

        val stepRange = oneToTen.step(3)

        for(x in stepRange) println("stepRange: $x")
        for(x in tenToOne.reversed()) println("Reversed: $x")

        /***** Conditionals *****/
        // > < >= <= == != && || !
        val age = 8
        // Normal if/else
        if(age < 5) {
            println("Go to preschool")
        }
        else if(age == 5) {
            println("Go to kindergarten")
        }
        else if((age > 5) && (age <= 17)) {
            val grade = age - 5
            println("Go to grade $grade")
        }
        else {
            println("Go to college")
        }

        // when
        when(age) {
            0, 1, 2, 3, 4 -> println("Go to preeschool")
            5 -> println("Go to kindergarten")
            in 6..17 -> {
                val grade = age - 5
                println("Go to grade $grade")
            }
            else -> println("Go to college")
        }

        /***** Loops *****/
        for(x in 1..10) {
            println("x: $x")
        }
        // You can import and use Java classes.
        val rand = Random()
        val magicNum = rand.nextInt(50) + 1

        var guess = 0
        while(magicNum != guess) {
            guess += 1
        }
        println("Magic number was: $guess")

        for(x in 1..20) {
            if(x % 2 == 0) {
                continue
            }
            println("Odd: $x")
            if(x == 15) break
        }

        var intArr: Array<Int> = arrayOf(3, 6, 9)
        for(i in intArr.indices) {
            println("Multiples of 3: ${intArr[i]}")
        }

        for((index, value) in intArr.withIndex()) {
            println("Index: $index Value: $value")
        }

        /***** Functions *****/
        // fun $name($params) : $returnType = / {}
        fun add(num1: Int, num2: Int) : Int = num1 + num2
        println("5 + 4 = ${add(5, 4)}")

        // Default values
        // Note for single line functions, return type doesn't need to be specified.
        fun subtract(num1: Int=1, num2: Int=1) = num1 - num2;
        println("5 - 4 = ${subtract(5, 4)}")
        println("4 - 5 = ${subtract(num2=5, num1=4)}")

        // Void functions use Unit
        fun sayHello(name: String) : Unit = println("Hello $name")
        sayHello("Paul")

        // Getting two values from a function.
        fun twoReturns(num: Int) : Pair<Int, Int> {
            return Pair(num + 1, num + 2)
        }
        val (two, three) = twoReturns(1)
        println("1 : $two $three")

        // Sending a variable number of parameters.
        fun getSum(vararg nums: Int) : Int {
            var sum = 0

            nums.forEach { n -> sum += n }
            return sum
        }
        println("Sum = ${getSum(1, 2, 3, 4, 5)}")

        // Function literals
        val multiply = { num1: Int, num2: Int -> num1 * num2 }
        println("5 * 3 = ${multiply(5, 3)}")

        // Factorial example with tail recursion
        fun fact(x: Int) : Int {
            tailrec fun factTail(y: Int, z: Int) : Int {
                if(y == 0) return z
                else return factTail(y - 1, y * z)
            }
            return factTail(x, 1)
        }
        println("5! = ${fact(5)}")

        // Higher order functions (Functions that accept or return another function)
        val numList = 1..20
        // If functions just have one parameter, you can reference it with the keyword 'it'
        val evenList = numList.filter { it % 2 == 0 }
        // Both work the same
        evenList.forEach { n -> println(n) }
        evenList.forEach { println(it) }

        // Returning a function
        // fun def : (return function param) -> return function return type { return function body }
        fun makeMathFunc(num1: Int) : (Int) -> Int = { num2 -> num1 * num2 }
        val multiply3With = makeMathFunc(3)
        println("5 * 2 = ${multiply3With(5)}")

        // Defining a function parameter
        // fun funcName( funParam: (funParam params) -> funParam return )
        fun mathOnList(numList: Array<Int>, myFunc: (num: Int) -> Int) {
            for(num in numList) {
                println("MathOnList: ${myFunc(num)}")
            }
        }

        val multiply2 = { num1: Int -> num1 * 2 }
        val exampleList = arrayOf(1, 2, 3, 4, 5)
        mathOnList(exampleList, multiply2)


        /***** Collections *****/
        // Lists
        var list1: MutableList<Int> = mutableListOf(1, 2, 3, 4, 5)
        val list2: List<Int> = listOf(1, 2, 3)

        list1.add(6)
        println("First: ${list1.first()}")
        println("Last: ${list1.last()}")
        println("Second: ${list1[1]}")
        println("Length: ${list1.size}")

        var list3 = list1.subList(0, 3)
        list3.clear()

        list1.remove(1) // Value
        list1.removeAt(1) // Index
        list1[2] = 10
        list1.forEach { println("Mutable list: $it") }

        // Maps
        val map = mutableMapOf<Int, Any?>()
        val map2 = mutableMapOf(
            1 to "Doug",
            2 to 25
        )

        map[1] = "Doug"
        map[2] = 25
        println("Map size: ${map.size}")
        map.put(3, "Pittsburgh")
        map.remove(2)

        for((x, y) in map) {
            println("Key: $x Value: $y")
        }

        // Collection Operators
        val numList2 = 1..20
        val listSum = numList2.reduce { x, y -> x + y }
        println("Reduce sum: $listSum")
        val listSum2 = numList2.fold(5) { x, y -> x + y }
        println("Fold sum (with initial value of 5): $listSum2")

        println("Evens: ${numList2.any { it % 2 == 0 }}") // Do any meet this condition? true
        println("Evens: ${numList2.all { it % 2 == 0 }}") // Do all meet this condition? false

        val greaterThanThree = numList2.filter { it > 3 }
        greaterThanThree.forEach { n -> println("> 3: $n") }
        greaterThanThree.forEach { println("> 3: $it") }

        // Map returns a new list after operating on it?
        val multipleBySeven = numList2.map { it * 7 }
        multipleBySeven.forEach { println("*7: $it") }

        /***** Exceptions *****/
        val divisor = 2
        try {
            if(divisor == 0) {
                throw IllegalArgumentException("Can't divide by 0.")
            }
            else {
                println("5 / $divisor = ${5.toFloat()/divisor}")
            }
        } catch(e: IllegalArgumentException) {
            println(e.message)
        }
    }

    /***** Null safety *****/
    // By default, you can't assign a value to be null.
    // var nullVal: String = null // error

    // you have to specify the variable can be null with '?'
    var nullVal: String? = null

    // Likewise with function return type singatures.
    fun returnNull(): String? {
        return null
    }

    var nullVal2 = returnNull()

    // Smart cast: If we provide a check like this, Kotlin will cast it to the appropriate value.
    if(nullVal2 != null) {
        println("${nullVal2.length}")
    }

    // Force/Not null Assertion operator: throws a NullPointerException if nullVal3 is null.
    var nullVal3 = nullVal2!!.length

    // Safe Call
    println("Safe call: ${nullVal2?.length}") // Should print null.
    nullVal2?.let { println(it.length) } // Shouldn't print.
    // If a chain like this contains null in the safe check, the right hand function is not called.
    // person?.job?.title = job.getTitle()

    // Elvis operator: Assign a value if the return could be null
    var nullVal4: String = returnNull() ?: "This is the value since we got null.."
    println(nullVal4)

    // Also valid uses of the Elvis operator (Useful for checking function args):
    // val name = person.getName() ?: throw IllegalArgumentException("Name required")
    // val age = person.getPersonalInfo() ?: return null
}
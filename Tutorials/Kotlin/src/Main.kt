

fun main(args : Array<String>) {
    println("Hello, world!")

    // Immutable variable (Unchangeable value).
    val name = "Jerry"
    // Mutable variable (Changeable value).
    var age = 25

    // Specifying data types.
    var bigInt: Int = Int.MAX_VALUE
    var smallInt: Int = Int.MIN_VALUE
    // Other types: Long Double Float Boolean(true, false) Short Byte Char.

    // Different ways to print information.
    println("Biggest Int: " + bigInt)
    // Using String interpolation AKA using syntax inside a string to get a value out.
    println("Smallest Int: $smallInt")

    // Loss of precision with floating numbers after the 15th place.
    var dblNum1: Double = 1.1111111111111111
    var dblNum2: Double = 1.1111111111111111
    println("Sum: " + (dblNum1 + dblNum2))

    // Using the keyword is to check data types.
    if(true is Boolean) {
        println("true is boolean")
    }
    var letterGrade = 'A'
    // Can have expressions in Strings.
    println("Is A a character: ${letterGrade is Char}")

    // Casting.
    println("3.14 to Int: " + (3.14.toInt()))
    println("A to Int: ${letterGrade.toInt()}")
    println("65 to Char: " +65.toChar())

    // String comparison.
    println("lol".equals("LOL"))

    /* Arrays. */
    var myArray = arrayOf(1, 1.23, "string")
    println(myArray[1])
    myArray[1] = 3.14

    println("Array Length: ${myArray.size}")
    println("PI in array: ${myArray.contains(3.14)}")
    var partArray = myArray.copyOfRange(0, 1)

    // USing lambdas to make an array of squared values.
    var sqrArray = Array(5, { x -> x * x})
    println(sqrArray.last())

    // Another way to initialize an array.
    var arr2: Array<Int> = arrayOf(1, 2, 3)

    // Ranges
    val oneToTen = 1..10
    val alpha = "A".."Z"
    for(n in oneToTen) println(n)

    print(alpha)



}
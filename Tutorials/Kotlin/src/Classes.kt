/**
 * Kotlin classes notes:
 *  1, No static methods.
 *  2. Classes and class functions are final by default unless marked as open.
 */

/***** Class Example *****/
open class Animal(val name: String, var height: Double, var weight: Double) {

    // Params are usually initialized here, and can be used as middleware to verify that the values are ok :)
    init {
        val regex = Regex(".*\\+.*")
        require(!name.matches(regex)) { "Animal name can't contain a nubmer!" }

        require( height > 0 ) { "Height must be greather than 0! "}
        require( weight > 0 ) { "Weight must be greather than 0! "}
    }

    open fun getInfo(): Unit {
        println("$name is $height tall and weighs $weight")
    }

}

/***** Inheritance Example *****/
// child class signature(params) : parentClass( child params that define parent params )
class Dog(name: String, height: Double, weight: Double, var owner: String) : Animal(name, height, weight) {

    // Functions marked as open can be overridden with the override keyword.
    override fun getInfo() : Unit {
        println("$name is $height tall and weighs $weight and is owned by $owner")
    }

}

/***** Interface Example *****/
interface Flyable {
    var flies: Boolean

    fun fly(distanceMilesFlown: Double): Unit
}
// You can call the constructor directly with the constructor keyword, not really required to include here?
class Bird constructor(name: String, height: Double, weight: Double, override var flies: Boolean) :
    Animal(name, height, weight),
    Flyable {

    override fun getInfo() {
        println("$name is $height tall and weighs $weight and is ${if(flies) "able" else "unable"} to fly.")
    }

    override fun fly(distanceMilesFlown: Double) {
        if(flies) {
            println("$name flies $distanceMilesFlown miles.")
        }
    }
}

fun main(args: Array<String>) {
    // Class
    val bowser = Animal("Bowser", 20.0, 13.5)
    bowser.getInfo()

    // Class using inheritance.
    val spot = Dog("Spot", 20.0, 14.5, "Paul Smith")
    spot.getInfo()

    // Class using inheritance and an interface.
    val tweety = Bird("Tweety", 2.0, 1.0, true)
    tweety.getInfo()
    if(tweety.flies) {
        tweety.fly(10.0)
    }
}
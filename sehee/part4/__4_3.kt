import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

// 3) 왕실의 나이트
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (x, y) = readLine().convertToXY()
    println(countNightMovement(x, y))
}

fun countNightMovement(x: Int, y: Int): Int {
    var count = 0

    val movement = listOf(
        Pair(2, 1),
        Pair(2, -1),
        Pair(1, 2),
        Pair(-1, 2),
        Pair(-1, 2),
        Pair(1, -2),
        Pair(-2, 1),
        Pair(-2, -1)
    )

    movement.map {
        val moveX = it.first
        val moveY = it.second
        if (x + moveX >= 1 && y + moveY >= 1 && x + moveX <= 8 && y + moveY <= 8) count++
    }

    return count
}

fun String.convertToXY(): Pair<Int, Int> {
    val alphabets = listOf(
        Pair("a", 1),
        Pair("b", 2),
        Pair("c", 3),
        Pair("d", 4),
        Pair("e", 5),
        Pair("f", 6),
        Pair("g", 7),
        Pair("h", 8)
    )

    val (alphabet, y) = substring(0, 1) to substring(1, 2).toInt()

    val x = alphabets.find {
        it.first == alphabet
    }?.second ?: 0

    return (x to y)
}
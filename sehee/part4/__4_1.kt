import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

// 1) 상하좌우
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val moves = readLine().split(' ')

    var (originX, originY) = 1 to 1

    for (i in moves.indices) {
        val (x, y) = convertAlphabetToCoordinate(moves[i])

        if (originX + x < 1 || originX + x > n ||
            originY + y < 1 || originY + y > n
        ) continue

        originX += x
        originY += y
    }

    println("$originX $originY")

}

fun convertAlphabetToCoordinate(str: String): Pair<Int, Int> {
    return when (str) {
        "R" -> {
            0 to 1
        }
        "L" -> {
            0 to -1
        }
        "U" -> {
            -1 to 0
        }
        else -> {
            1 to 0
        }
    }
}
import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

// 3) 숫자 카드 게임
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(' ').map { it.toInt() }
    val arr = Array<IntArray>(n) { IntArray(m) }
    val minValue = IntArray(n) { Int.MAX_VALUE }

    for (i in arr.indices) {
        arr[i] = readLine().split(' ').map { it.toInt() }.toIntArray()
        arr[i].minOrNull()?.let {
            minValue[i] = min(minValue[i], it)
        }
    }

    println(minValue.maxOrNull())
}
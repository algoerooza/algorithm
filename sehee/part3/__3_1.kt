import java.io.BufferedReader
import java.io.InputStreamReader

// 1) 거스름 돈 주기
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readLine().toInt()
    val arr = arrayOf(500, 100, 50, 10)
    var count = 0

    for (i in arr.indices) {
        if (n == 0) return

        val quotient = n / arr[i]
        count++
        n -= (arr[i] * quotient)
    }
    println(count)
}
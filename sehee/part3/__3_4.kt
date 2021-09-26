import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

// 4) 1이 될때까지
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var (n, k) = readLine().split(' ').map { it.toInt() }

    var result = 0
    while (n != 1) {
        if (n % k == 0) {
            n /= k
        } else {
            n -= 1
        }

        result += 1
    }

    println(result)
}
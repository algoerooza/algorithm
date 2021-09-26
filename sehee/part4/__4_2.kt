import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

// 2) 시각
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    var count = 0
    for (i in 0..n) {
        for (j in 0 until 60) {
            for (k in 0 until 60) {
                val hms = i.toString() + j.toString() + k.toString()
                if (hms.contains("3")) {
                    count++
                }
            }
        }
    }

    println(count)
}

import java.io.BufferedReader
import java.io.InputStreamReader

// 2) 큰 수의 법칙
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    // 배열의 크기 n, 숫자가 더해지는 횟수 m, k번 반복
    val (n, m, k) = readLine().split(' ').map { it.toInt() }
    val arr = readLine()
        .split(' ')
        .map { it.toInt() }
        .toIntArray()
        .sortedByDescending { it }

    var total = 0
    var count = 0

    while (true) {
        if (m == count) break

        repeat(k) {
            total += arr[0]
            count += 1
        }

        if (m == count) break

        total += arr[1]
        count += 1
    }

    println(total)
}
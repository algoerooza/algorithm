import java.io.BufferedReader
import java.io.InputStreamReader

var m = -1
var n = -1

// 5.3 음료수 얼려먹기
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    readLine().split(' ')
        .map { it.toInt() }
        .apply {
            m = first()
            n = last()
        }

    val arr = Array(m) { IntArray(n) { 0 } }

    var count = 0
    for (i in 0 until m) {
        arr[i] = readLine().split(' ').map { it.toInt() }.toIntArray()
    }

    for (i in 0 until m) {
        for (j in 0 until n) {
            if (dfs(arr, i, j)) count++
        }
    }

    println(count)
}

fun dfs(arr: Array<IntArray>, x: Int, y: Int): Boolean {
    if (x <= -1 || y <= -1 || x >= m || y >= n) return false
    // 방문처리
    if (arr[x][y] == 0) {
        arr[x][y] = 1

        dfs(arr, x + 1, y)
        dfs(arr, x, y - 1)
        dfs(arr, x, y + 1)
        dfs(arr, x - 1, y)

        return true
    }

    return false
}
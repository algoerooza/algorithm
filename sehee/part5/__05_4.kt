import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.ArrayDeque

var m = 0
var n = 0

// 5.4 미로탈출
// 방문할 때마다 arr 의 숫자가 1씩 더해지는 형태임.
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    readLine().split(' ')
        .map { it.toInt() }
        .apply {
            m = first()
            n = last()
        }

    val arr = Array(m) { IntArray(n) { 0 } }

    for (i in 0 until m) {
        arr[i] = readLine().map { it.toString().toInt() }.toIntArray()
    }


    println(dfs(arr, 0, 0))
}

fun dfs(arr: Array<IntArray>, x: Int, y: Int): Int {
    val queue = ArrayDeque<Pair<Int, Int>>().apply {
        add(x to y)
    }

    val xy = listOf(
        0 to 1,
        0 to -1,
        1 to 0,
        -1 to 1
    )

    while (queue.isNotEmpty()) {
        // 처음 시작한 xy 좌표 pop
        val (qx, qy) = queue.pop()

        for (i in 0 until 4) {
            // 나아갈 xy 좌표 + 현재 위치 좌표 qx qy
            val x1 = xy[i].first + qx
            val y1 = xy[i].second + qy

            // 범위에 벗어나면 continue
            if (x1 <= -1 || y1 <= -1 || x1 >= m || y1 >= n) continue

            // 내가 간 곳이 길이 맞다면(1), 이전에 도착한 값에 + 1
            // 후헤 현재 내가 있는 좌표를 queue 에 넣기
            if (arr[x1][y1] == 1) {
                arr[x1][y1] = arr[qx][qy] + 1
                queue.add(x1 to y1)
            }
        }
    }

    return arr.last().last()
}
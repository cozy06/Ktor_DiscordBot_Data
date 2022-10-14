package cozy06.com

import io.ktor.server.engine.*
import io.ktor.server.netty.*
import cozy06.com.plugins.*
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.io.BufferedReader
import java.io.File
import java.io.FileReader

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0") {
        configureRouting()
        GlobalScope.launch {
            delay(200)
            println("Connecting...")
            delay(1800)
            println("Connected")
            while(true) {
                PythonCommunicate()
            }
        }
    }.start(wait = true)
}

suspend fun PythonCommunicate() {
    val project_path = System.getProperty("user.dir")
    val todopath = File(project_path + "/src/main/kotlin/cozy06/com/DiscordBot/DATA/ConnectionJava/todo.txt")
    while(true) {
        if (todopath.exists()) {
            val inFile1 = BufferedReader(FileReader(todopath))
            var sLine1: Array<String?>
            var todo = arrayOfNulls<String>(2)
            var i = 0

            while (inFile1.readLine().also { sLine1 = arrayOf(it) } != null) {
                var split = sLine1[0]?.split(":\\")
                todo[i] = split?.get(1)
                i++
            }
            inFile1.close()

            var PlayerID = todo[0]
            var todolist = todo[1]

            var DataPath = File(project_path + "/src/main/kotlin/cozy06/com/DiscordBot/DATA/" + PlayerID + "_DATA.TXT")
            if (DataPath.exists()) {
                println("-----------START connection-----------")
                var inFile2 = BufferedReader(FileReader(DataPath))
                var sLine2: Array<String?>
                var PlayerData = arrayOfNulls<String>(2)
                var t = 0

                while (inFile2.readLine().also { sLine2 = arrayOf(it) } != null) {
                    var split = sLine2[0]?.split(":\\")
                    PlayerData[t] = split?.get(1)
                    println(PlayerData[t])
                    t++
                }
                inFile2.close()
                println(todolist)

                var result: Boolean = todopath.delete()
                if (result) {
                    println("------------END connection------------")
                    //break
                } else {
                    //println("No File")
                }
                if(todolist == "END") {
                    println("Task END")
                    break
                }
            }
        }
        else {
            //println("No File")
        }
    }
}

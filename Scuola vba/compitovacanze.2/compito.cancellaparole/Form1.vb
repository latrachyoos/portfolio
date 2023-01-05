Public Class Form1
    Dim N As Integer = 20
    Dim p(N - 1) As String

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim par As String
        Dim i As Integer
        FileOpen(1, "parole.txt", OpenMode.Input)
        Do While Not EOF(1)
            i += 1
            par = LineInput(1)
            p(i - 1) = par
            ListBox1.Items.Add(par)
        Loop
        FileClose(1)
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim lett As String
        If Trim(Len(TextBox1.Text)) = 1 Then
            lett = TextBox1.Text
            For i = 0 To N - 1
                If LCase(lett) = LCase(Mid(p(i), 1, 1)) Then
                    cancella(i)
                    i -= 1
                End If
            Next
            carica()
        End If

    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim lett As String
        Dim lun, i As Integer
        Dim trov As Boolean = True
        If Trim(Len(TextBox1.Text)) > 1 Then
            lett = TextBox1.Text
            lun = Len(lett)
            Do While i < N - 1 And trov
                If lun <= Len(p(i)) Then
                    If LCase(lett) = LCase(Mid(p(i), 1, lun)) Then
                        trov = False
                    End If
                End If
                i += 1
            Loop
        End If
        If trov Then
            MessageBox.Show("non trovato")
        Else
            MessageBox.Show("trovato")
        End If
    End Sub

    Sub carica()
        ListBox1.Items.Clear()
        For i = 0 To N - 1
            ListBox1.Items.Add(p(i))
        Next
    End Sub

    Sub cancella(ByVal i As Integer)
        For t = i To N - 2
            p(t) = p(t + 1)
        Next
        N -= 1
    End Sub
End Class

Public Class Form1
    Dim Nmax As Integer = 50
    Dim X(Nmax - 1) As String
    Dim Y(Nmax - 1) As String
    Dim N As Integer
    Const file As String = "stringa.txt"
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        caricafile()
    End Sub

    Sub caricafile()
        Dim S() As String
        FileOpen(1, file, OpenMode.Input)
        Do While Not EOF(1)
            S = Split(LineInput(1), ";")
            X(N) = S(0)
            Y(N) = S(1)
            N += 1
        Loop
        FileClose(1)
        visua(Y, X)
    End Sub

    Sub scaricafile()
        FileOpen(1, file, OpenMode.Output)
        Dim S As String
        For i = 0 To N - 1
            S = X(i) & ";" & Y(i)
            PrintLine(1, S)
        Next
        FileClose(1)
    End Sub

    Sub visua(ByRef Y() As String, ByRef X() As String)
        ListBox1.Items.Clear()
        For i = 0 To N - 1
            ListBox1.Items.Add(X(i) & "    -    " & Y(i))
        Next
    End Sub

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        If Trim(TextBox1.Text) <> "" And Trim(TextBox2.Text) <> "" Then
            X(N) = Trim(TextBox1.Text)
            Y(N) = Trim(TextBox2.Text)
            N += 1
            visua(Y, X)
            'TextBox1.Clear()
            'TextBox2.Clear()
        End If
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        If RadioButton1.Checked Then
            ordina(X)
        Else
            ordina(Y)
        End If
        visua()
    End Sub

    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        scaricafile()
    End Sub

    Sub ordina(ByRef V() As String)
        Dim con As Boolean = True
        Dim p As Integer
        Do While con
            con = False
            For i = 0 To V.GetUpperBound(0) - 1 - p
                If V(i) > V(i + 1) Then
                    con = True
                    change(V(i), V(i + 1))
                End If
            Next
            p += 1
        Loop
    End Sub

    Sub change(ByRef A As String, ByRef B As String)
        Dim C As String = A
        A = B
        B = C
    End Sub
End Class

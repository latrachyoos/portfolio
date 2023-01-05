Public Class Form1
    Dim X() As String = {"a", "f", "c", "d", "z", "p"}
    Dim N As Integer = 10
    Dim Y(N - 1) As String

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        carica(Y)
        visua(Y)
    End Sub

    Sub visua(ByRef Y() As String)
        ListBox1.Items.Clear()
        For i = 0 To N - 1
            ListBox1.Items.Add(Y(i))
        Next
    End Sub

    Sub carica(ByRef Y() As String)
        Randomize()
        Dim l As String
        Dim i As Integer
        Do
            l = LCase(Chr(Int(Rnd() * 26) + 65))
            If controllo(l, X) Then
                Y(i) = l
                i += 1
            End If
        Loop Until i > N - 1
    End Sub

    Function controllo(ByVal l As String, ByRef X() As String) As Boolean
        Dim con As Boolean = True
        Dim i As Integer
        Do
            If l = X(i) Then
                con = False
            End If
            i += 1
        Loop Until Not con Or i > X.GetUpperBound(0)
        Return con
    End Function

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim l As String
        If Trim(Len(TextBox1.Text)) = 1 Then
            l = Trim(TextBox1.Text)
            canc(l, Y)
        End If
    End Sub

    Sub canc(ByVal l As String, ByRef Y() As String)
        Dim i As Integer
        Dim spot As Boolean = False
        Do While Not spot And i < Y.GetUpperBound(0)
            If Y(i) = l Then
                spot = True
            End If
            i += 1
        Loop
        If spot Then
            cancella(i - 1, Y)
        End If
    End Sub

    Sub cancella(ByVal i As Integer, ByRef Y() As String)
        For k = i To Y.GetUpperBound(0) - 1
            Y(k) = Y(k + 1)
        Next
        Y(Y.GetUpperBound(0)) = 0
        N -= 1
        visua(Y)
    End Sub
End Class

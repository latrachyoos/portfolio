Public Class Form1
    Const max As Integer = 16
    Dim x(max) As Integer

    Sub crea()
        Randomize()
        svuota()
        Dim N, num As Integer
        N = 0
        Dim Y As Integer = max + 1
        Do While N < max
            num = Int(Rnd() * Y) - 1
            If Not esiste(num) Then
                x(N) = num
                N += 1
            End If
        Loop
        visualizza()
    End Sub

    Sub svuota()
        For i = 0 To max - 1
            x(i) = 0
        Next
    End Sub

    Function esiste(ByVal num As Integer) As Boolean
        Dim n As Integer = 0
        esiste = False
        Do While Not esiste And n < max
            If num = x(n) Then
                esiste = True
            End If
            n += 1
        Loop
    End Function

    Sub visualizza()
        ListBox1.Items.Clear()
        For i = 0 To max - 1
            ListBox1.Items.Add(x(i))
        Next
    End Sub

    Sub assegnabutton()
        Dim n As Integer
        For Each btn As Button In Panel1.Controls
            If x(n) <> -1 Then
                btn.Text = x(n)
            Else
                btn.Text = ""
            End If
            n += 1
        Next
    End Sub

    Private Sub casual_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles casual.Click
        Do
            If controllo() = True Then
                crea()
                assegnabutton()
            End If
        Loop Until controllo()
    End Sub

    Function controllo() As Boolean
        controllo = False
        Dim c As Integer
        For i = 0 To max - 2
            For k = i + 1 To max - 1
                If x(i) > x(k) Then
                    c += 1
                End If
            Next
        Next
        If c Mod 2 = 0 Then
            controllo = True
        End If
    End Function

    Private Sub btn_0_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btn_15.Click, btn_13.Click, btn_12.Click, btn_0.Click, btn_1.Click, btn_2.Click, btn_3.Click, btn_4.Click, btn_5.Click, btn_6.Click, btn_7.Click, btn_8.Click, btn_9.Click, btn_10.Click, btn_11.Click, btn_14.Click
        Dim str As String
        Dim s() As String
        Dim dif, somma As Integer
        str = sender.name
        s = Split(str, "_")
        dif = vuoto() - s(1)
        somma = vuoto() + s(1)
        'MessageBox.Show(dif & vbCrLf & vuoto() & vbCrLf & s(1))
        If somma <> 7 And somma <> 15 And somma <> 23 Then
            If dif = -1 Or dif = 1 Or dif = 4 Or dif = -4 Then
                swap(x(s(1)), x(vuoto()))
                visualizza()
                assegnabutton()
            End If
        End If
        If controlla() = True Then
            MessageBox.Show("forse hai vinto")
        End If
    End Sub

    Sub swap(ByRef x As Integer, ByRef y As Integer)
        Dim z As Integer
        z = y
        y = x
        x = z
    End Sub

    Function vuoto() As Integer
        Do While x(vuoto) <> -1
            vuoto += 1
        Loop
    End Function

    Function controlla() As Boolean
        controlla = True
        Dim k As Integer = 0
        For i = 0 To max - 2
            k = +i
            Do While controlla And k < max - 1
                If x(i) < x(k) Then
                    controlla = False
                End If
                k += 1
            Loop
        Next
    End Function
End Class


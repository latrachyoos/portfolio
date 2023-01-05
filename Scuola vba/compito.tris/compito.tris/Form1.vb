Public Class Form1
    Const N As Integer = 3
    Dim M(N - 1, N - 1) As String
    Dim giocatore As String
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        azzera()
        
    End Sub

    Sub azzera()
        For Each btn As Button In Panel1.Controls
            btn.Text = ""
            btn.Enabled = True
        Next
        T = 0
        scelta()
        For r = 0 To N - 1
            For c = 0 To N - 1
                M(r, c) = ""
            Next
        Next
    End Sub

    Sub scelta()
        Randomize()
        If RadioButton1.Checked Or RadioButton2.Checked Then
            If RadioButton1.Checked Then
                giocatore = RadioButton1.Text
            Else
                giocatore = RadioButton2.Text
            End If
        Else
            If Int(Rnd() * 2) = 0 Then
                giocatore = "X"
            Else
                giocatore = "O"
            End If
        End If
    End Sub

    Sub vittoria()
        MessageBox.Show("il giocatore " & giocatore & " ha vinto")
        For Each btn As Button In Panel1.Controls
            btn.Enabled = False
        Next
    End Sub

    Sub cambia()
        If giocatore = "X" Then
            giocatore = "O"
        Else
            giocatore = "X"
        End If
    End Sub
    Dim T As Integer

    Private Sub btn00_Click(sender As System.Object, e As System.EventArgs) Handles btn00.Click, btn01.Click, btn02.Click, btn10.Click, btn11.Click, btn12.Click, btn20.Click, btn21.Click, btn22.Click
        Dim R, C As Integer
        R = Mid(sender.name, 4, 1)
        C = Mid(sender.name, 5, 1)

        If M(R, C) = "" Then
            T += 1
            M(R, C) = giocatore
            sender.text = giocatore
            controlla(R, C)
            cambia()
        Else
            MessageBox.Show("casella occupata")
        End If
        If T = 9 Then
            For Each btn As Button In Panel1.Controls
                btn.Enabled = False
            Next
            MessageBox.Show("è finito")
        End If
    End Sub

    Sub controlla(ByVal R As Integer, ByVal C As Integer)
        If T > 4 And T < 10 Then
            If controllaOR(R, giocatore) Or controllaVER(C, giocatore) Then
                vittoria()
            End If
            If R = C Then
                If diagonalePRI(giocatore) Then
                    vittoria()
                End If
            ElseIf R + C = N - 1 Then
                If diagonaleSEC(giocatore) Then
                    vittoria()
                End If
            End If
        End If
    End Sub

    Function controllaOR(ByVal ind As Integer, ByVal simbolo As String) As Boolean
        Dim c As Integer
        Dim continua As Boolean = True
        Do
            If M(ind, c) <> simbolo Then
                continua = False
            End If
            c += 1
        Loop Until c > N - 1 Or Not continua
        Return continua
    End Function

    Function controllaVER(ByVal ind As Integer, ByVal simbolo As String) As Boolean
        Dim r As Integer
        Dim continua As Boolean = True
        Do
            If M(r, ind) <> simbolo Then
                continua = False
            End If
            r += 1
        Loop Until r > N - 1 Or Not continua
        Return continua
    End Function

    Function diagonalePRI(ByVal simbolo As String) As Boolean
        Dim i As Integer = 0
        Dim continua As Boolean = True
        Do
            If M(i, i) <> simbolo Then
                continua = False
            End If
            i += 1
        Loop Until Not continua Or i > N - 1
        Return continua
    End Function

    Function diagonaleSEC(ByVal simbolo As String) As Boolean
        Dim i As Integer = 0
        Dim continua As Boolean = True
        Do
            If M(i, (N - 1) - i) <> simbolo Then
                continua = False
            End If
            i += 1
        Loop Until Not continua Or i > N - 1
        Return continua
    End Function

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        azzera()
    End Sub
End Class

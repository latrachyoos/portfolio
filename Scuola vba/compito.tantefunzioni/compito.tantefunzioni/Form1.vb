Public Class Form1
    Const max As Integer = 100
    Dim x(max) As Integer
    Dim Nstop As Integer = 0

    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        create_casual()
    End Sub

    Sub create_casual()
        Dim N As Integer
        Do While N <> 100 And Nstop < max
            Randomize()
            N = Rnd() * 51 + 50
            x(Nstop) = N
            ListBox1.Items.Add(N)
            Nstop += 1
        Loop
        MessageBox.Show(Nstop)
    End Sub

    Function conta(ByVal n As Integer) As Integer
        For i = 0 To Nstop
            If x(i) = n Then
                conta += 1
            End If
        Next
    End Function

    Function media(ByVal n As Integer) As Integer
        Dim count As Integer = 0
        
        For i = 0 To Nstop
            If x(i) > n Then
                media += x(i)
                count += 1
            End If

        Next
            media /= count

    End Function

    Function containf(ByVal n As Integer) As Integer
        For i = 0 To Nstop
            If x(i) < n And x(i) Mod 2 = 0 Then
                containf += 1

            End If
        Next
    End Function

    Function somma(ByVal n As Integer) As Integer
        For i = 0 To Nstop
            If i Mod 2 = 1 And x(i) < n Then
                somma += x(i)
            End If
        Next
    End Function

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim n As Integer
        If IsNumeric(TextBox1.Text) And TextBox1.Text >= 50 And TextBox1.Text <= 100 Then
            n = TextBox1.Text
            MessageBox.Show("conta uguali: " & conta(n))
            If n <> 100 Then
                MessageBox.Show("media maggiori: " & media(n))
            Else
                MessageBox.Show("Non ci sono numeri maggiori")
            End If

            MessageBox.Show("inferiori e pari: " & containf(n))
            MessageBox.Show("somma inferiori in posizione dispari: " & somma(n))
        Else
            MessageBox.Show("Ritenta sarai più fortunato")
        End If
    End Sub
End Class

Public Class Form1
    Dim A() As Integer = {10, 5, 24, 68, 4, 10, 12, 20, 3, 5}
    Dim b() As Integer = {"165", "175", "160", "190", "168", "190", "175", "180", "171", "166"}
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        N = UBound(A) + 1
        Label1.Text = "Ci sono " & parità() & " numeri con stessa parità"
        Label2.Text = "Ci sono " & multipli() & " numeri multipli"
        visua()
    End Sub

    Dim N As Integer

    Sub visua()
        ListBox1.Items.Clear()
        For i = 0 To N - 1
            ListBox1.Items.Add(A(i))
        Next
    End Sub

    Function parità()
        Dim num As Integer
        For i = 0 To N - 1
            If A(i) Mod 2 = 0 And b(i) Mod 2 = 0 Then
                num += 1
            ElseIf A(i) Mod 2 <> 0 And b(i) <> 0 Then
                num += 1
            End If
        Next
        Return num
    End Function

    Function multipli()
        Dim num As Integer
        For i = 0 To N - 1
            If b(i) Mod A(i) = 0 Then
                num += 1
            End If
        Next
        Return num
    End Function

    Sub cancella(ByVal ind As Integer)
        For i = ind To N - 2
            A(i) = A(i + 1)
            b(i) = b(i + 1)
        Next
        N -= 1
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim ind As Integer
        If Trim(Len(TextBox1.Text)) = 1 And IsNumeric(TextBox1.Text) Then
            ind = Math.Abs(Int(TextBox1.Text))
            cancella(ind)
        End If
        visua()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim n1, n2, temp(N) As Integer
        If IsNumeric(TextBox2.Text) And IsNumeric(TextBox3.Text) Then
            n1 = Trim(TextBox2.Text)
            n2 = Trim(TextBox3.Text)
            N += 1
            Array.Resize(A, N + 1)
            Array.Resize(b, N + 1)
            If n1 < n2 Then
                A(N - 1) = n1
                b(N - 1) = n2
            Else
                b(N - 1) = n1
                A(N - 1) = n2
            End If
        End If
        visua()
    End Sub
End Class
'9. Utilizza i seguenti 2 vettori paralleli
'Dim A() As Integer = {10, 5, 24, 68, 4, 10, 12, 20, 3, 5}
'Dim b() as integer={"165","175","160","190","168","190","175","180","171","166",}
'Creare gli algoritmi che permettono di 
'A. Contare in quanti casi ci sono elementi corrispondenti aventi la stessa parità
'B. in quanti casi il valore presente in B è un multiplo del corrispondente valore presente in A
'C. Eliminare da entrambi i vettori il valore che si trova in una posizione indicata da un utente 
'mediante un numero inserito in una TextBox.
'D. Inserire due nuovi valori (uno in ciascun vettore
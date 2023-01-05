Public Class Form1
    Dim R As Integer = 9
    Dim C As Integer = 5
    Dim M(R - 1, C - 1) As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        carica()
        visualizza()
        pari()
    End Sub

    Sub carica()
        Randomize()
        For i = 0 To R - 1
            For k = 0 To C - 1
                M(i, k) = Int(Rnd() * 9) + 1
            Next
        Next
    End Sub

    Sub visualizza()
        dgvdati.Columns.Clear()
        dgvdati.Rows.Clear()
        dgvdati.ColumnCount = C
        dgvdati.Rows.Add(R - 1)
        For i = 0 To R - 1
            For k = 0 To C - 1
                dgvdati.Rows(i).Cells(k).Value = M(i, k)
            Next
        Next
    End Sub

    Sub pari()
        Dim P(R * C - 1), n As Integer
        For i = 0 To R - 1
            For k = 0 To C - 1
                If M(i, k) Mod 2 = 0 Then
                    P(n) = M(i, k)
                    n += 1
                End If
            Next
        Next
    End Sub
    Dim O(R * C - 1), n As Integer
    Sub ordina()
        For i = 0 To R - 1
            For k = 0 To C - 1
                O(n) = M(i, k)
                n += 1
            Next
        Next

        For i = 0 To n - 2
            For k = i To n - 1
                If O(i) > O(k) Then
                    cambia(i, k)
                End If
            Next
        Next
        n = 0
        For i = 0 To R - 1
            For k = 0 To C - 1
                M(i, k) = O(n)
                n += 1
            Next
        Next
    End Sub

    Sub cambia(ByVal x As Integer, ByVal y As Integer)
        Dim z As Integer
        z = O(x)
        O(x) = O(y)
        O(y) = z
    End Sub

    Private Sub dgvdati_CellContentClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgvdati.CellClick
        Dim ind, somma As Integer
        ind = dgvdati.CurrentCell.ColumnIndex
        For i = 0 To R - 1
            somma += M(i, ind)
        Next
        MessageBox.Show(somma)
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        ordina()
        visualizza()
    End Sub
End Class
'8. Creare un programma che permetta di effettuare le seguenti operazioni:
'a. Caricare una matrice (9 righe x 5 colonne) con numeri casuali compresi tra 1 e 9
'b. Visualizzare la matrice
'c. Caricare in un vettore tutti i numeri pari presenti nella matrice
'd. Caricare in un vettore tutti i valori presenti nella matrice, ordinare il vettore in modo crescente, 
'ricaricare i valori ordinati all'interno della matrice
'e. Sommare i valori presenti in una colonna selezionata dall'utente
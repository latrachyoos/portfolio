Public Class Form1
    Dim N As Integer = 5
    Dim C(N - 1, N - 1), O(N - 1, N - 1) As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        carica()
        visualizza()
        media()
        For i = 0 To N - 1
            ListBox1.Items.Add(Max(i))
        Next
        Label2.Text = "La somma della diagonale principale é : " & som1()
        Label3.Text = "La somma della diagonale secondaria é : " & som2()
        Label4.Text = "La somma delle diagonali é : " & (som2() + som1() - C(N \ 2, N \ 2))
        inverti()
        Label5.Text = "La somma dei numeri pari a sinistra della diagonale é : " & som3()
        Label6.Text = "La media dei numeri a destra della diagonale é : " & med()
    End Sub

    Sub carica()
        Randomize()
        For i = 0 To N - 1
            For k = 0 To N - 1
                C(i, k) = Int(Rnd() * N) + 1
            Next
        Next
    End Sub

    Sub visualizza()
        dgvdati.Columns.Clear()
        dgvdati.Rows.Clear()
        dgvdati.ColumnCount = N
        dgvdati.Rows.Add(N - 1)
        For i = 0 To N - 1
            For k = 0 To N - 1
                dgvdati.Rows(i).Cells(k).Value = C(i, k)
            Next
        Next
    End Sub

    Sub media()
        Dim somma As Decimal
        For i = 0 To N - 1
            For k = 0 To N - 1
                somma += C(i, k)
            Next
        Next
        somma /= N ^ 2
        Label1.Text = "La media dei valori é: " & somma
    End Sub

    Function Max(ByVal ind As Integer) As Integer
        Max = C(0, ind)
        For i = 1 To N - 1
            If Max < C(i, ind) Then
                Max = C(i, ind)
            End If
        Next
    End Function

    Function som1() As Integer
        Dim somma As Integer
        For i = 0 To N - 1
            somma += C(i, i)
        Next
        Return somma
    End Function

    Function som2() As Integer
        Dim somma As Integer
        For i = 0 To N - 1
            somma += C(N - 1 - i, i)
        Next
        Return somma
    End Function

    Sub inverti()
        For i = 0 To N - 1
            For k = 0 To N - 1
                O(i, k) = C(k, i)
            Next
        Next
    End Sub

    Function Sup(ByVal som As Integer) As Integer
        Dim num, somma As Integer
        For i = 0 To N - 1
            somma = 0
            For k = 0 To N - 1
                somma += C(i, k)
            Next
            If somma > som Then
                num += 1
            End If
        Next
        Return num
    End Function

    Private Sub dgvdati_CellContentClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgvdati.CellClick
        Dim ind, somma As Integer
        ind = dgvdati.CurrentCell.RowIndex
        For i = 0 To N - 1
            somma += C(ind, i)
        Next
        MessageBox.Show(Sup(somma) & " righe hanno somma superiore")
    End Sub

    Function som3() As Integer
        Dim somma As Integer
        For i = 1 To N - 1
            For k = 0 To i - 1
                If C(i, k) Mod 2 = 0 Then
                    somma += C(i, k)
                End If
            Next
        Next
        Return somma
    End Function

    Function med() As Decimal
        Dim media As Decimal
        Dim num As Integer
        For i = 0 To N - 2
            For k = i + 1 To N - 1
                media += C(i, k)
                num += 1
            Next
        Next
        media /= num
        Return media
    End Function
End Class
'7. Dopo aver caricato con numeri casuali una matrice quadrata N x N, scrivere il codice che permette di:
'A. Visualizzare la matrice in una datagridview
'B. Calcolare la media dei valori presenti nella matrice
'C. Visualizzare in una lista il valore massimo di ciascuna colonna dopo aver creato una funzione che 
'restituisce il max di una colonna il cui indice viene passato come parametro
'D. La somma degli elementi che si trovano lungo la diagonale principale (creare una funzione)
'E. La somma degli elementi che si trovano lungo la diagonale secondaria (creare una funzione)
'F. La somma degli elementi che si trovano lungo le due diagonali, facendo riferimento alle funzioni 
'sviluppate ai punti F e G. Ricorda che nel caso di numero di righe/colonne dispari, l’elemento centrale 
'non deve essere sommato 2 volte (ossia alla somma va sottratto l’elemento centrale)
'G. Creare una nuova matrice invertendo le righe con le colonne
'H. Individuare quante righe presentano una somma maggiore della somma dei valori presenti su una 
'riga selezionata dall'utente
'I. Calcolare la somma dei valori pari che si trovano a sinistra della diagonale principale
'J. Calcolare la media dei valori che si trovano a destra della diagonale principale